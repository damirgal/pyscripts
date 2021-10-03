import time
from selenium import webdriver
import re

driver = webdriver.Firefox(executable_path=r'E:\pit\geckodriver\geckodriver.exe')
driver.get("http://81.30.218.195:81/tekl/")
time.sleep(0.5)
ord = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div/div[2]/div/ul')
time.sleep(0.5)
ord.click()

#ord1 = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div/div[2]/div/ul/li[5]/label')
ord1 = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/ul/li[3]/label')
time.sleep(0.5)
ord1.click()

file2 = open('C:/Users/admin/Desktop/big/bashrts/bashrts_'+dt.strftime("%Y-%m-%d-%H.%M.%S")+'.txt', 'a', encoding="utf8")
file2.write('addr;uzel;date;T1;T2;G1;G2;M1;M2;Q;W;VNR\n')

#for i in range(1, 619):
for i in range(1, 631):
    time.sleep(0.4)
#for i in range(1, 2):
    x = '//*[@id="main-wrapper"]/div/div[2]/div/ul/li[3]/ul/li['+ str(i) +']/a'
    ord2 = driver.find_element_by_xpath(x)
    ord2.click()
    ord3 = driver.find_element_by_xpath('//*[@id="fluid-wrapper"]/div')
    #print(ord3.text)
    
    a = driver.find_element_by_xpath(x).text
    print(a)
    
    tip = re.search(r'(Теплоснабжение[\w\s\№-]+)\n', ord3.text)
    if tip:
        tip = tip.group(1)
        #print(tip)
    else:
        tip = ''
        
    d = re.search(r'Данные за ([\d\w\s,:]+)\n', ord3.text)
    if d:
        d = d.group(1)
        d = d.replace(' янв ', '.01.')
        d = d.replace(' фев ', '.02.')
        d = d.replace(' мар ', '.03.')
        d = d.replace(' апр ', '.04.')
        d = d.replace(' май ', '.05.')
        d = d.replace(' июн ', '.06.')
        d = d.replace(' июл ', '.07.')
        d = d.replace(' авг ', '.08.')
        d = d.replace(' сен ', '.09.')
        d = d.replace(' окт ', '.10.')
        d = d.replace(' ноя ', '.11.')
        d = d.replace(' дек ', '.12.')
        d = d.replace(',', '')
        #print(d)
    else:
        d =''
    
    

    t1 = re.search(r'T1: (\d+\.\d+) C', ord3.text)
    if t1:
        t1 = t1.group(1)
        #print(t1)
    else:
        t1 = '0'

    t2 = re.search(r'T2: (\d+\.\d+) C', ord3.text)
    if t2:
        t2 = t2.group(1)
        #print(t2)
    else:
        t2 = '0'

    g1 = re.search(r'G1: ([\d\.]+) м', ord3.text)
    if g1:
        g1 = g1.group(1)
        #print(g1)
    else:
        g1 = '0'

    g2 = re.search(r'G2: ([\d\.]+) м', ord3.text)
    if g2:
        g2 = g2.group(1)
        #print(g2)
    else:
        g2 = '0'

    m1 = re.search(r'М1: ([\d.]+) т', ord3.text)
    if m1:
        m1 = m1.group(1)
        #print(m1)
    else:
        m1 = '0'

    m2 = re.search(r'М2: ([\d.]+) т', ord3.text)
    if m2:
        m2 = m2.group(1)
        #print(m2)
    else:
        m2 = '0'

    q = re.search(r'Q накоп: ([\d.]+) Гкал', ord3.text)
    if q:
        q = q.group(1)
        #print(q)
    else:
        q = '0'

    w = re.search(r'W: ([\d.]+) Гкал/ч', ord3.text)
    if w:
        w = w.group(1)
        #print(w)
    else:
        w = '0'

    vnr = re.search(r'ВНР: ([\d.]+) ч', ord3.text)
    if vnr:
        vnr = vnr.group(1)
        #print(vnr)
    else:
        vnr = '0'


    res =str(a) + ';'+ str(tip) + ';' + str(d) + ';' + str(t1) + ';' + str(t2) + ';' + str(g1) + ';' + str(g2) + ';' + str(m1) + ';' + str(m2) + ';' + str(q) + ';' + str(w) + ';' + str(vnr) + '\n'
    file2.write(res)
file2.close()
