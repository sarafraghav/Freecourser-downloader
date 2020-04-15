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
links = open('failed.log').readlines()
#CODE
 #REGEXLINKEXTRACTOR--------------------------------------------------------------------------
 
for x in links:
 zippy = open('zippysharelinks.txt', 'w')
 zippy.write(x)
 zippy.close()   
 #MEDIALINKFINDER------------------------------------------------------------------------------

 subprocess.call([r'link_extractor.bat'])
 if open('links.txt').read().strip() == '':
   while open('links.txt').read().strip() == '':
     subprocess.call([r'link_extractor.bat'])
     print('hi')
 
 #Downloader-----------------------------------------------------------------------------------
 subprocess.call([r'downloader.bat'])