import time
import schedule
from datetime import datetime
from stock_schedule import conferencia
from arquivo_confidencial import WATCH_LIST, NUMBERS

horario_comercial = int(datetime.now().strftime('%H'))


if __name__ == '__main__':
    schedule.every(1).to(20).minutes.do(conferencia, watch_list=WATCH_LIST,
        numeros_cadastrados=NUMBERS)
    while True:
        if  10 <= horario_comercial <= 17:
            schedule.run_pending()
        else:
            time.sleep(900)
        time.sleep(15)
