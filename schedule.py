from time import time, sleep
from sched import scheduler
from time import strftime




def printa_hora():
   print('Hora: %s' % strftime("%Hh%Mmin%Ss"))


scheduler.every(10).seconds.do(printa_hora)
