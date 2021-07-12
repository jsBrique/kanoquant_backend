from ..app.watcher.tuport import tuport
import pandas as pd
import os
import sys
class Analysis:
    def __init__(self):
        pass
        self.dataport=tuport()
        self.prepare()
    def ETFdownload(self):
        today_all=self.dataport.get_ETFlist()
        today_all.to_csv('dataset/ETFlist.csv',encoding='utf-8')
    def prepare(self):
        self.today_all= pd.read_csv('dataset/ETFlist.csv')
        self.codes=list(self.today_all['symbol'])
        self.names=list(self.today_all['name'])
        self.states=list(self.today_all['state'])
        self.num=len(self.codes)

    def ETFread(self):


        for i in range(self.num):
            
            print('读取基金'+self.names[i]+str(self.codes[i]))
            hist_data=self.dataport.getETFbars(str(self.codes[i]))
            hist_data.to_csv('dataset/ETFhist/ETF_%s_%s'%(str(self.codes[i]),self.names[i]))

        return self.today_all

    def read_ETFcsv(self,code):
       
        self.ETFcsvList=os.listdir('dataset/ETFhist')
        for l in self.ETFcsvList:
            if code in l:
                return pd.read_csv('dataset/ETFhist/'+l)

    def find(self,day_num):
        res=[]
        for i in range(self.num):
            data=pd.read_csv('dataset/ETFhist/ETF_%s_%s'%(str(self.codes[i]),self.names[i]))
            #print(data['close'].iloc[-1])
            try:
                fg=False
                for d in range(1,day_num):
                    fg=data['close'].iloc[-d]>data['close'].iloc[-(d+1)]
                    if fg==False:
                        break

                if fg:
                    res.append([self.codes[i],self.names[i]])
            except:
                print('err',self.codes[i],self.names[i])
        return res
    def findrealtime(self,day_num):
        res=self.find(day_num)
        codelist=[]
        for c in res:
            codelist.append(c[2:])
        realtime_res=self.dataport.get_realtime(codelist)
        return realtime_res

if __name__ == '__main__':
    ans=Analysis()
    #ans.ETFdownload()
    #print(list(ans.ETFread()))
    res=ans.findrealtime(5)
    print(res)
    # for r in res:
    #     print(r[0],r[1])
    #print(list(ans.ETFread()['基金代码']))

    