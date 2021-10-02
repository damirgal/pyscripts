# -*- coding: utf-8 -*-
import re
import time
import os
import serial
import sys
import datetime
import pymysql
from urllib.request import Request, urlopen
import urllib
import urllib.error
import urllib.request
#import smbus
from dateutil.relativedelta import relativedelta



dt = datetime.datetime.now()
date1 = dt.day


file = 'ya.html'


req0='https://yandex.ru/pogoda/ufa?lat=54.819809&lon=56.116405'
req = Request(req0, headers={'User-Agent': 'Mozilla/5.0'} )
try:
    webpage = urlopen(req)
except urllib.error.HTTPError:
    s = 'connect error'
    connerror+=1
    print(s, '(',connerror,')')
else:
    html = webpage.read()
    page0='ya.html'
    page = open(page0, 'wb')
    page.write(html)
    page.close()





if os.path.exists(file):
    page = open(file, 'r', encoding="utf8")
    f = page.read()

    #f_temp=re.search(r'fact__temp fact__temp_size_s" role="text"><span class="temp__value">(.*?)</span>', f)
    #f_temp=re.search(r'Текущая температура</span><span class="temp__value">(.*?)</span>', f)
    f_temp=re.search(r'Текущая температура</span><span class="temp__value temp__value_with-unit">(.*?)</span>', f)
    if f_temp:
        f_temp=f_temp.group(1)
        f_temp = f_temp.replace('−', '-')
        f_temp = f_temp.replace('+', '+')
        #print (f_temp)


    #f_temp1=re.search(r'Ощущается как</div><div class="term__value"><div class="temp" role="text"><span class="temp__value">(.*?)</span>', f)
    f_temp1=re.search(r'Ощущается как</div><div class="term__value"><div class="temp" role="text"><span class="temp__value temp__value_with-unit">(.*?)</span>', f)
    
    
    
    if f_temp1:
        f_temp1=f_temp1.group(1)
        f_temp1 = f_temp1.replace('−', '-')
        f_temp1 = f_temp1.replace('+', '+')
        #print (f_temp1)


    p=re.search(r'icon_pressure-white term__fact-icon" aria-hidden="true"></i>(.*?)<span', f)
    if p:
        p=p.group(1)
        #print (p)


    h=re.search(r'icon icon_humidity-white term__fact-icon" aria-hidden="true"></i>(.*?)</div>', f)
    if h:
        h=h.group(1)
        #print (h)

    w=re.search(r'wind-airflow-white term__fact-icon" aria-hidden="true"></i><span class="wind-speed">(.*?)</span>', f)
    #w=re.search(r'term__value" aria-label="Ветер: (.*?) Метров в секунду', f)

    if w:
        w=w.group(1)
        #print (w)

        #date1 = str(date1)
        #usl = 'condition day-anchor i-bem" data-bem=\'{"day-anchor":{"anchor":'+date1+'}}\'>(.*?)</div>'



    wd=re.search(r'role="text">([А-Я,\-\s]{,5})</abbr><i class="icon icon_size_12 icon_wind', f)
    if wd:
        wd=wd.group(1)
        #print (p)


    #cond=re.search(r'>(.*?)</div><div class="term term_orient_h fact__feels-like', f)
    cond=re.search(r'condition day-anchor i-bem" data-bem=\'{"day-anchor":{"anchor":\d{1,2}}}\'>(.*?)</div>', f)
    #cond = re.search(r'}}\'>(.*?)</div><div class="term term_orient_h fact__feels-like', f)
    #cond=re.search(r'usl', f)
    #cond=re.search(r'}}\'>(.*?)</div>', f)

        
    if cond:
        cond=cond.group(1)
        if cond == 'Ясно':
            c ='clear'
        elif cond == 'Малооблачно':
            c = 'cloud1'
        elif cond == 'Облачно с прояснениями':
            c = 'cloud2'
        elif cond == 'Пасмурно':
            c = 'cloud3'
        elif cond == 'Небольшой дождь':
            c = 'rain1'
        elif cond == 'Дождь':
            c = 'rain2'
        elif cond == 'Сильный дождь':
            c = 'rain3'
        elif cond == 'Сильный дождь, гроза':
            c = 'rain3'
        elif cond == 'Дождь со снегом':
            c = 'rai+sn'
        elif cond == 'Небольшой снег':
            c = 'snow1'
        elif cond == 'Снег':
            c = 'snow2'
        elif cond == 'Снегопад':
            c = 'snow3'
        #print(c)
        
        

        

bd = datetime.datetime(2021, 2, 22)
now = datetime.datetime.now()
delta = relativedelta(now, bd)
#(delta.months, '+', delta.days, sep='')




#открываем порт
ser = serial.Serial('COM13', 9600, dsrdtr = 1,timeout = 0)
#ser = serial.Serial('/dev/ttyACM0', 9600, dsrdtr = 1,timeout = 0)


#text1=f_temp+' a '+f_temp1+' P:'+p + str(proc)
text1=f_temp+' a '+f_temp1+' P:'+p + str(delta.months) + '+' + str(delta.days)
#+' as '+f_temp1+' P:'+p
#text2='H: '+h+' W:'+w+'m/s'
#text2= c +' W:' + str(w) + ' ' + str(week) + '+' + str(week_ost) + ' ' + str(ost.days)
text2= c +' W:' + str(w) + ' ' + str(dt.hour) + ':' + str(dt.minute)
#str('{:.0f}'.format(h_dat))
#text2= c






text1=text1.ljust(20, ' ')
text2=text2.ljust(20, ' ')

text=text1+text2

#if w != 'Штиль':
w = w.replace(",", ".")
w = float(w)

#else:
 #   w = 0

#h =  h[0 : -1]
#w = float(w)





print('--------------------------------------')
#print (text + h + ' '+ wd)
print (text)

time.sleep(3)

#text = '123456781234567812345678901234567890'
text = text.encode('cp866')
ser.write(text)
ser.close()







        

    
        
        
