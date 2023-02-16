# importing the requests library
from fastapi import Depends
import requests,datetime
from sqlalchemy.orm import Session,scoped_session

from events import database, models
import schedule
import time,pandas,json
from .sendalert import *
'2023-01-07 17:22:07.294457'
 
FN_SESSION=''
AN_SESSION=''

date=datetime.datetime.today()
print(date)
print(type(date))

def bio_data(engine=database.get_engine()):
        
    '''URL="https://jsonplaceholder.typicode.com/todos"
    r = requests.get(url = URL)
    
    # extracting data in json format
    data = r.json()'''
    data= ["staff1@gmail.com","staff2@gmail.com","staff3@gmail.com","staff4@gmail.com","staff5@gmail.com","staff6@gmail.com","staff5@gmail.com","staff8@gmail.com","staff9@gmail.com","staff10@gmail.com","staff11@gmail.com"]
    data=[ ["12", "staff12@gmail.com"], ["13 ", "staff13@gmail.com"], ["3", "staff3@gmail.com"], ["4", "staff4@gmail.com"], ["19", "staff19@gmail.com"], ["1", "staff1@gmail.com"], ["18", "staff18@gmail.com"], ["15", "staff15@gmail.com"], ["10", "staff10@gmail.com"], ["20", "staff15@gmail.com"], ["7", "staff7@gmail.com"]]
    data=[i[1] for i in data]
    
    with engine.connect() as conn:
        conn.execute(
                text("INSERT INTO presentstaff('date','data') VALUES('{}','{}')".format(datetime.datetime.today().strftime("%Y-%m-%d"),json.dumps(data)))
            )
        conn.commit()
    return data


get_db=database.get_db

'''
db:Session = Depends(get_db) --> did not work not sure why??

'''
'''
def get_today_event(date,db: scoped_session=next(get_db())):
    events=db.query(models.Event).filter(models.Event.date==str(date).split(' ')[0]).first() 
    print(events)  #.first() is impo

get_today_event(date)
'''

from sqlalchemy import text
import ast
import random
def get_today_event(event_session,engine=database.get_engine()):
    print('in')
 #   present=bio_data()
    present=[]
    with engine.connect() as conn:
        present_staff=conn.execute(text("SELECT * from presentstaff WHERE date='{}'".format(datetime.datetime.today().strftime("%Y-%m-%d"))))
        conn.commit()
        for i in present_staff:
            present= ast.literal_eval(i[2])
    
#    print("here ::::::::",present_staff)
 
    
    with engine.connect() as conn:
        events = conn.execute(text("SELECT * FROM events WHERE date='{}'".format(datetime.datetime.today().strftime("%Y-%m-%d"))))
        #print(events)
        
        print("Starting........"+event_session)
        for event in events:
            print("here")
            print("details :",(event[0],event[1],event[2],event[3],event[4],event[5],event[6]),event[2].split(' ')[0]==str(date).split(' ')[0],event_session==event[3])
            if event[2].split(' ')[0]==str(date).split(' ')[0] and event_session==event[3]:#datetime obj to str
                backup=[y for x,y in ast.literal_eval(event[6])]# y= email of backup staff
                print('backup list :',len(backup))
                lis=[y for x,y in ast.literal_eval(event[5])]# y= email of staff
                print('lis',lis)
                fin_lis=[]
                try:
                    for email in lis:
                        if email not in present:
                            alternative=random.choice(backup)
                            print('alternative',alternative)
                            fin_lis.append(alternative)
                            backup.remove(alternative)
                            print(email,'absent')
                        else:
                            fin_lis.append(email)
                        print(email,'--------------------------------')
                except :
                    print('unable to procees event')#more no of staffs absent than backup staff
                sendMail(date,event_session,fin_lis)
            print('##############################################################################')

import threading

def order_sequence():
    bio_data()  

def scheduler():
    schedule.every().day.at("11:03").do(lambda : bio_data())
    schedule.every(20).seconds.do(lambda: get_today_event(event_session='FN'))
    schedule.every(20).seconds.do(lambda: get_today_event(event_session='AN'))


    while True:
    
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)

t1=threading.Thread(target=scheduler)
t1.start()


'''
1-- check if backup staff is present 
    else :
        bring in random staff from present who is not in staff_lis or backup_lis

2-- send mail to backup staff stating they have exam duty


'''