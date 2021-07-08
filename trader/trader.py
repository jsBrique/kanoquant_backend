import easytrader
user=easytrader.use('ths')
user.connect(r'C:/gfzqrzrq/xiadan.exe')
print(user.balance)
#print(user.today_trades)
user.buy('000776', price=15.253, amount=100)
#183300149889
#183300141707