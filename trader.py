from datetime import datetime

import backtrader as bt  # 升级到最新版
import matplotlib.pyplot as plt  # 由于 Backtrader 的问题，此处要求 pip install matplotlib==3.2.2
import akshare as ak  # 升级到最新版
import pandas as pd
import random 
import pyfolio as pf
from backtrader_plotting import Bokeh
# plt.rcParams["font.sans-serif"] = ["SimHei"]
# plt.rcParams["axes.unicode_minus"] = False
def data_source(code='002646'):
    # 利用 AKShare 获取股票的后复权数据，这里只获取前 6 列
    stock_hfq_df = ak.stock_zh_a_minute(symbol=code, period='1', adjust="qfq").iloc[:, :6]

    stock_hfq_df=stock_hfq_df.dropna(axis = 0)

    # 处理字段命名，以符合 Backtrader 的要求
    stock_hfq_df.columns = [
        'date',
        'open',
        'high',
        'low',
        'close',
        'volume',
    ]
    for i in range(1,len(stock_hfq_df.columns)):
        stock_hfq_df[stock_hfq_df.columns[i]]=pd.to_numeric(stock_hfq_df[stock_hfq_df.columns[i]])

    # 把 date 作为日期索引，以符合 Backtrader 的要求
    stock_hfq_df.index = pd.to_datetime(stock_hfq_df['date'])
    print(stock_hfq_df)
    return stock_hfq_df


class MyStrategy(bt.Strategy):
    """
    主策略程序
    """
    params = (("maperiod", 20),       
         ('period', 9),
        ('period_dfast', 3),
        ('period_dslow', 3),)  # 全局设定交易策略的参数

    def __init__(self):
        """
        初始化函数
        """
        self.data_close = self.datas[0].close  # 指定价格序列
        # 初始化交易指令、买卖价格和手续费
        self.order = None
        self.last_price=0
        self.buy_price = None
        self.buy_comm = None
        # 添加移动均线指标
        self.now_max=0
        self.lines.top=bt.indicators.BollingerBands(self.datas[0],period=20,devfactor=0.5).top
        self.lines.bot=bt.indicators.BollingerBands(self.datas[0],period=20,devfactor=0.5).bot
        self.lines.mid=bt.indicators.BollingerBands(self.datas[0],period=20,devfactor=0.5).mid
        self.kd = bt.indicators.StochasticFull(
            self.datas[0],
            period=self.p.period,
            period_dfast=self.p.period_dfast,
            period_dslow=self.p.period_dslow,
        )

        self.l.K = self.kd.percD
        self.l.D = self.kd.percDSlow
        self.l.J = self.K * 3 - self.D * 2
    def next(self):
        """
        执行逻辑
        """
        #print(self.data_close[0])
        # if not self.position: 
        #     if self.data_close[0]>10 and self.data_close[0]<15:
        #         self.order = self.buy(size=100)
        # else:
        #     if self.data_close[0]>15:
        #         self.order = self.sell(size=100)
        # if self.order:  # 检查是否有指令等待执行,
        #     return
        # # 检查是否持仓
        #print(self.position)
        mount=0
        if not self.position:  # 没有持仓
            if self.l.J[0] > self.l.K[0] and self.l.J[-1] < self.l.K[-1] :  # 执行买入条件判断：收盘价格上涨突破20日均线
                amount=int((self.broker.getcash()/self.data_close[0])/100.0)*100
                self.order = self.buy(size=100)  # 执行买入
                print("buy")
                self.last_price=self.data_close[0]
                self.now_max= self.last_price
        elif self.last_price>0:
            
            v=self.data_close[0]/self.last_price -1.0
            if self.now_max<self.data_close[0]:
                self.now_max=self.data_close[0]
            mv=(self.data_close[0]/self.now_max) -1.0
            fv=(self.now_max/self.last_price)-1.0
            if fv<=0:
                fv=0
            if   mv < -0.04*(1/(1+fv*100)) or v >0.05 :  # 移动止损
                self.order = self.sell(size=100)  # 执行卖出



if __name__ == "__main__":
    cerebro = bt.Cerebro()  # 初始化回测系统
    data_s=data_source("sz123033")
    start_date = datetime(2021, 5, 1)  # 回测开始时间
    end_date = datetime(2021, 7, 28)  # 回测结束时间
    data = bt.feeds.PandasData(dataname=data_s, fromdate=start_date, todate=end_date)  # 加载数据
    cerebro.adddata(data,name='600196')  # 将数据传入回测系统
    
    cerebro.addstrategy(MyStrategy)  # 将交易策略加载到回测系统中
    start_cash = 20000
    cerebro.broker.setcash(start_cash)  # 设置初始资本为 100000
    cerebro.broker.setcommission(commission=0.0005)  # 设置交易手续费为 0.2%
    cerebro.run()  # 运行回测系统

    port_value = cerebro.broker.getvalue()  # 获取回测结束后的总资金
    pnl = port_value - start_cash  # 盈亏统计

    print(f"初始资金: {start_cash}\n回测期间：{start_date.strftime('%Y%m%d')}:{end_date.strftime('%Y%m%d')}")
    print(f"总资金: {round(port_value, 2)}")
    print(f"净收益: {round(pnl, 2)}")
    b=Bokeh(style='bar',plot_mode='single')
    cerebro.plot(b)  # 画图
