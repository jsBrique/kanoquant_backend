import numpy as np

class Strag:
    def __init__(self,r=0.03):
        self.r=r

    def pipline(self,account):
        for i in range(len(account)):
            cost=account[i]['cost']
            has = account[i]['has']
            value=account[i]['value']
            risk=self.calc_risk(value,cost,has)
            account[i]['risk']=risk
        return account
    
    def calc_risk(self,nowvalue,cost,amount):
        costvalue = cost*amount
        return (nowvalue - costvalue)/1-self.r