from gf_port import gf_API 
from userdata import Account,AccountData
import time
watcher_api=gf_API()
account_db=AccountData(username='dobriq',
                apikey='233')
time.sleep(3)
while True:
    
    data=watcher_api.get_pdata()
    if data is not None:
        account_db.position=data
        account_db.save()
    time.sleep(5)