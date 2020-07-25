import time
import schedule
from datetime import datetime
from stock_schedule import conferencia

watch_list = [['HGTX3',15.00, 16.13, 15.64],['MGLU3',84.00, 87.78, 85.04],['EZTC3',40.00, 41.09, 40.99], ['GRND3', 7.30, 8.27, 8.06],]
numeros_cadastrados = ['554891784586','555596985884']


if __name__ == '__main__':
    try:
        conferencia(watch_list, numeros_cadastrados)
    except Exception as e:
        print(e)
