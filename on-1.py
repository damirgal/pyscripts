# включение реле

import RPi.GPIO as GPIO
import datetime


GPIO.setwarnings(False)  # Отключить предупреждения

# инициализация по номеру пина на гребенке коннектора GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)  # установка пина на вывод
GPIO.output(11, 0)  # установка значения 0 для пина 11 (включение реле)

# запись в лог-файл время включения реле
text = 'ON1: ' + \
    str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + '\n'
f = open('log_on_off.txt', 'a')
f.write(text)
f.close()
