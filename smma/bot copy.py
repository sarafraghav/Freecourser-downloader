#IMPORTS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re
import os
#VARIABLES
links = ''
#CODE
driver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.get("https://freecourser.com/tai-lopez-smma-2-0/")
time.sleep(1)
driver.close()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
div = soup.findAll('a',{"class":"zippyshare_link"})
for line in div:
  links += line
#-----------------------------------------------------------------------------------
html = open(links).read()
zippy = open('zippysharelinks.txt', 'w')
soup = BeautifulSoup(html)

for a in soup.find_all('a', href=True):
    m = re.match(r"https://href.li/\?(.*)", a['href'])
    zippy.write(m.group(1))
    zippy.write('\n')


os.system('cmd /c "python zippyshare.py --in-file zippysharelinks.txt"')

lst = open('links.txt').readlines()
lst.sort(key= lambda x: int(x.split('.')[-1]))
print(''.join(lst))
open('links.txt','w').write(''.join(lst)) 

os.system('cmd /c " wget "')