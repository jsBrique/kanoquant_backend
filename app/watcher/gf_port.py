from selenium import webdriver
import time
import json
import os
import threading
import pickle
from flask_mongoalchemy import MongoAlchemy
#人民币持仓参考盈亏 /html/body/div[1]/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div[3]
#总资产 /html/body/div[1]/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div[1]/b
#刷新按钮 /html/body/div[1]/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/text()
#持仓列表 /html/body/div[1]/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[3]/div[2]/div/div/div[2]




asset_path='/html/body/div[1]/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div[1]/b'
profit_path='/html/body/div[1]/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div[3]'
position_path='/html/body/div[1]/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[3]/div[2]/div/div/div[2]'
tbody_path='/html/body/div[1]/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/table/tbody'
fresh_btn_path='/html/body/div[1]/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div[1]/div[2]'
table_fresh_path='/html/body/div[1]/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/div[1]/div/span'
login_username_path='/html/body/div[4]/div/div[2]/div/div[2]/form/div[2]/input'
trader_path='/html/body/div[1]/div/header/div[2]/div/div[2]/div/button[3]'

class gf_API:
    
    def __init__(self):
        # option = webdriver.ChromeOptions()
        # option.add_argument(r"--user-data-dir=C:\\Users\\huang\\AppData\\Local\\Google\\Chrome\\User Data")
        self.position_data=None
        self.driver = webdriver.Chrome()
        self.login()
        self.loop_th=threading.Thread(target=self.loop)
        self.loop_th.start()

        # if os.path.exists('cookie.bin'):
        #     with open('cookie.bin','r') as f:
        #         cookie=pickle.load(f)
        #     self.driver.add_cookie(cookie)
        # else:
            
        #     self.save_cookie()
    def __del__(self):
        self.loop_th.terminate()

    def save_cookie(self):
        cookie=self.driver.get_cookies()
        with open('cookie.bin','w') as f:
            pickle.dump(f,cookie)
    
    def login(self):
        url = 'https://hippo.gf.com.cn/'
        self.driver.get(url)
        print("等待加载，然后打开登陆页面")
        check=input("自动填充账号？(yes):")
        if 'y' in check:
            self.driver.find_element_by_xpath(login_username_path).send_keys('183300149889')

        check=input("请完成登陆操作,然后输入yes:")
        
        #self.driver.find_element_by_xpath(trader_path).click()
        if 'y' not in check:
            print("退出")
            exit()
        self.driver.maximize_window()

    def get_assets(self):
        return self.driver.find_element_by_xpath(asset_path).text
    
    def get_profit(self):
        return self.driver.find_element_by_xpath(profit_path).text
    
    def get_positionlist(self):
        return self.driver.find_element_by_xpath(tbody_path).text

    def allrefresh(self):
        self.driver.find_element_by_xpath(fresh_btn_path).click()
    
    def refresh(self):
        self.driver.find_element_by_xpath(table_fresh_path).click()
    def struct_data(self,position_str):
        res=[]
        position_strlines=position_str.splitlines()
        for i,pstr in enumerate(position_strlines): 
            
            plist=pstr.split(' ')
            resline={
                'id':i,
                'stockclass':plist[0],
                'stockname':plist[1],
                'stockcode':plist[2],
                'has':float(plist[3].replace(',','')),
                'canuse':float(plist[4].replace(',','')),
                'cost':float(plist[5].replace(',','')),
                'price':float(plist[6].replace(',','')),
                'value':float(plist[7].replace(',','')),
                'profit':float(plist[8].replace(',','')),
                'rate':float(plist[9].strip('%').replace(',',''))
            }
            res.append(resline)
        return res
            
    def get_pdata(self):
        return self.position_data

    def loop(self):
        fix=input('确认列表')
        while True:
            try:
                # os.system("clear")
                # print("======================================")
                # print('今日浮动盈亏:',self.get_profit())
                # print('总资产:',self.get_assets())
                # print('仓位列表\n',self.struct_data(self.get_positionlist()))
                # print('======================================')
                self.position_data=self.struct_data(self.get_positionlist())
                time.sleep(5)
                self.refresh()
                time.sleep(5)
            except Exception as e:
                print(str(e))
                fix=input('请修复页面')
    
if __name__=='__main__':
    gf=gf_API()
    gf.loop()

