#coding: utf-8
import RPi.GPIO as GPIO
import sys
import time

len_arg = len(sys.argv)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin = {1: 11, 2: 13, 3: 15}  # словарь пинов
st = {0: 1, 1: 0}  # словарь состояний реле


if (len_arg == 2 and (sys.argv[1] == '-h') or (sys.argv[1] == '--help') or (sys.argv[1] == '/?')):
    print(
        "Параметры для управления реле:\nимя_файла.py [номер розетки] [1/0 - вкл/выкл] [время работы реле в секундах]\nномер розетки и действие - обязательные параметры,\nвремя работы - необязательный параметр")

elif (len_arg == 3):
    GPIO.setup(pin[int(sys.argv[1])], GPIO.OUT)
    GPIO.output(pin[int(sys.argv[1])], st[int(sys.argv[2])])

elif (len_arg == 4):
    GPIO.setup(pin[int(sys.argv[1])], GPIO.OUT)
    GPIO.output(pin[int(sys.argv[1])], 0)
    time.sleep(int(sys.argv[3]))
    GPIO.output(pin[int(sys.argv[1])], 1)

else:
    print('Error. Please, input right parameters')