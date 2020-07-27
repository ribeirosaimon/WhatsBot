import time
import schedule
from datetime import datetime
from stock_schedule import conferencia
from arquivo_confidencial import WATCH_LIST, NUMBERS

if __name__ == '__main__':
    schedule.every().wednesday.at('10:15').do(conferencia(watch_list=WATCH_LIST,
        numeros_cadastrados=NUMBERS))   
    while True:
        schedule.run_pending()
        time.sleep(1)
