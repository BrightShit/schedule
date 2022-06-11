import os
from datetime import datetime
import schedule
import time
from selenium import webdriver

def get_day():
    return datetime.today().strftime('%A')
    
def morning_a():
    try:
        os.startfile(get_day()+'.png')
    except:
        print("Have fun! its Saturday")
schedule.every().day.at("07:30").do(morning_a)

while 1:
    schedule.run_pending()
    time.sleep(1)



print(get_day(), morning_a())

