import schedule
import time
from main import main

schedule.every().hour.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)


