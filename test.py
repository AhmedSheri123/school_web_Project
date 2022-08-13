import pytz, datetime
"""print(datetime.datetime.now(pytz.timezone('Asia/Baghdad')))
print(datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('Asia/Baghdad')), '%Y-%m-%d %H:%M:%S'))
"""



"""
import sqlite3, datetime

conn = sqlite3.connect('db.sqlite3')

cur = conn.cursor()

PassData = '''SELECT id, username, passDate, GuardianNumber FROM accounts_passdata'''

PassData_Definded = '''SELECT GuardianNumber FROM accounts_passdata WHERE is_Definded=True'''

PassData_Definded = cur.execute(PassData_Definded).fetchall()
print(PassData_Definded)
PassData = cur.execute(PassData).fetchall()

for id, username, pass_date, num in PassData:
    pass_date = datetime.datetime.strptime(pass_date, "%Y-%m-%d %H:%M:%S")
    print(id, username, pass_date, num)"""




"""import os
from re import T

def check_ping():
    hostname = "web.whatsapp.com"
    response = os.system("ping -n 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = True
    else:
        pingstatus = False
    
    return pingstatus

"""

numdays = 30

base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]
weekDaysAr = ["الاثنين", "الثلاثاء", "الاربعاء", "الخميس", "الجمعة", "السبت", "الاحد"]
for i in date_list:
    print(i.date())
    print(i.strftime("%A"))
    print(weekDaysAr[i.weekday()])