
'''
import numpy,pandas
def exceltodb(engine=database.get_engine()):
    # "commit as you go"
    with engine.connect() as conn:
        df=pandas.read_csv('E:/class.csv')
        for name,floor,block in df.to_numpy():
            print(name)
            conn.execute(
                text("INSERT INTO classrooms VALUES('{}','{}','{}')".format(name,floor,block))
            )
        conn.commit()
exceltodb()'''


'''
schedule.every(10).seconds.do(order_function)
schedule.every().day.at("08:47").do(bedtime)
schedule.every().day.at("08:47").do(bedtime)

while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)'''