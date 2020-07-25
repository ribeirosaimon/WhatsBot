import time
import schedule
from datetime import datetime
from stock_schedule import schedule_conferencia


if __name__ == '__main__':
    schedule.every(60).seconds.do(schedule_conferencia)
    while True:
        schedule.run_pending()
        time.sleep(1)
