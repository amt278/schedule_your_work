import schedule
from schedule import every, repeat 
import time

@repeat(every(2).seconds, msg='marhaba')
def talk(msg):
    print(msg)

#j = schedule.every(3).seconds.do(talk, msg='ahlen') # el default 1, fi hagat gher seconds
#schedule.every.day.at('12:00').do(talk)
#schedule.every().hour.until(time(12, 0, 0)).do(talk)
#schedule.every(1).to(5).do(talk) # random number ma ben 1 w 5 seconds

counter = 0

while True:
    schedule.run_pending()
    time.sleep(1)
    counter += 1
    if counter == 10: # b3d 10 sec abort
        schedule.cancel_job(j)
        break
