#IMPORTS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re
import os
from selenium.webdriver.firefox.options import Options
import subprocess
#VARIABLES
links = ''
#CODE

 #SCRAPER-------------------------------------------------------------------------------------  
print("SCRAPER STARTED")
options = Options()
options.headless = True
driver = webdriver.Firefox(firefox_options=options,  executable_path='geckodriver.exe')
driver.get("https://freecourser.com/tai-lopez-smma-2-0/")
time.sleep(1)
html = driver.page_source
driver.close()
soup = BeautifulSoup(html, 'html.parser')
div = soup.findAll('a',{"class":"zippyshare_link"})
print("SCRAPERD SUCCESSFULLY")
 #EXTRACTOR-----------------------------------------------------------------------------------
try: 
 for video in range(138,len(div)):
  zippy = open('zippysharelinks.txt', 'w')
  soup = BeautifulSoup(str(div[video]))
  a =  soup.find('a', href=True)
  print('LINK EXTRACED SUCCESSFULLY : ' + str(a))
 #REGEXLINKEXTRACTOR--------------------------------------------------------------------------

  if 'href' in a['href']:
   m = re.match(r"https://href.li/\?(.*)", a['href'])
   zippy.write(m.group(1))
   final_link = m.group(1)
  else:
    zippy.write(a['href'])
    final_link = a['href']
  zippy.close()   
  print("Regex Completed Successfully : " + str(final_link))
 #MEDIALINKFINDER------------------------------------------------------------------------------

  subprocess.call([r'link_extractor.bat'])
  if open('links.txt').read() == '':
   while open('links.txt').read() == '':
     subprocess.call([r'link_extractor.bat'])

 #Downloader-----------------------------------------------------------------------------------
  subprocess.call([r'downloader.bat'])
except:
  with open('failed.txt','a') as f:
    f.write(str(div[video]) + ':' + str(video))
  pass
