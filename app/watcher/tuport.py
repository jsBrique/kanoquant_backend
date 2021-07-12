import baostock as bs
import pandas as pd
import logging
import datetime
import time
import tushare as ts
import akshare as ak
from matplotlib import pyplot as plt
# from pyecharts.charts import Candlestick

class tuport:
    def __init__(self,logger=None):
        self.init_loger(logger)
        self.lg=bs.login()
        if self.lg.error_code!='0':
            self.logger.error("连接数据接口失败,"+"错误代码"+self.lg.error_code+"错误原因:"+self.lg.error_msg)
        else:
            self.logger.info("连接成功")
        ts.set_token("98a8b7ec01e51387e8c3259323a940aaadac74326611abf9e7e5e8fb")
        self.tupro = ts.pro_api()
    def __del__(self):
        bs.logout()

    def fundflow(self,code='601919.sh'):
        codesp=code.split('.')
        return ak.stock_individual_fund_flow(stock=codesp[0], market=codesp[1])

    def code_detail(self,code='601919'):
        market='sh'
        spec='main'
        if code[0:3] in ['600','601','603']:#沪
            market='sh'
            spec='main'
        elif code[0:3] in ['000','001']:#深
            market='sz'
            spec='main'
        elif code[0:3]=='002':#中小板
            market='sz'
            spec='SME'
        elif code[0:3]=='300':#创业板
            market='sz'
            spec='GEM'
        elif code[0:3]=='688':#科创板
            market='sh'
            spec='KCB'
        else:
            market=''
            spec=''
        return code+'.'+market
        
        


    def getETFbars(self,code='510300.sh'):
        codesp=code.split('.')
        return ak.fund_etf_hist_sina(code)

    def get_all(self,deST=True,ETFOnly=False,BondOnly=False):
        if ETFOnly:
            self.all_market=ak.fund_em_etf_fund_daily()
        elif BondOnly:
            self.all_market=ak.bond_zh_hs_cov_spot()
        else:
            self.all_market=ak.stock_zh_a_spot_em()
        return self.all_market
        #return self.tupro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    # def get_days(self,stockcode="sh.601919",days=30,freq="d",save=False):
        

    def get_k_bar(self,stockcode="sh.601919",days=30,freq='60',save=False):
        today = datetime.date.today()
        preday=today - datetime.timedelta(days=days)
        rs = bs.query_history_k_data_plus(stockcode,
            "date,time,code,open,high,low,close,volume,amount",
            start_date=str(preday), end_date=str(today),
            frequency=freq, adjustflag="2")
#     #### 打印结果集 ####
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        if save==True:
            result.to_csv("./dataset/"+stockcode+'_'+str(today)+'_'+str(preday)+'_'+freq+'K.csv', index=False)
        return result
    
    # def codetrans(self,ex='sh',code='601919'):
    #     return [ex+'.'+code,code,ts.get_stock_basics()]
    def get_ETFlist(self):
        return ak.fund_etf_category_sina(symbol="ETF基金")        
    def get_LOFlist(self):
        return ak.fund_etf_category_sina(symbol="LOF基金")

    def get_realtime(self, stockcode=["601919","002312"]):
        return ts.get_realtime_quotes(stockcode)

    def save_csv(self,result,path,filename):
        result.to_csv("./history_A_stock_k_data.csv", index=False)

    def load_csv(self,path):
        return pd.read_csv(path)

    def init_loger(self,logger):
        if logger is None:
            self.logger = logging.getLogger('tuport')
            self.logger.setLevel(logging.INFO)
            hdr = logging.StreamHandler()
            formatter = logging.Formatter('[%(asctime)s] %(name)s:%(levelname)s: %(message)s')
            hdr.setFormatter(formatter)
            # 给logger添加上handler
            self.logger.addHandler(hdr)
        else:
            self.logger=logger
import os
if __name__ == "__main__":
    stockdata=tuport()
    while True:
        
        print(stockdata.get_all())
        #print(stockdata.get_ETFlist())
        time.sleep(30)
        
    # histdata=stockdata.get_k_bar()
    # close=list(map(float,histdata['close'].tolist()))
    # boll=talib.BBANDS(histdata['close'],timeperiod=20)
    # plt.plot(histdata['time'],close)
    # plt.plot(histdata['time'],boll[0])
    # plt.plot(histdata['time'],boll[1])
    # plt.plot(histdata['time'],boll[2])
    # plt.show()
    #print(boll[0])
    # print(stockdata.get_realtime())
    
