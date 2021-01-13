from datetime import datetime
from time import sleep


while True:
    print(datetime.now(), end='\r')
    sleep(1)
