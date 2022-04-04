import sys
sys.path.insert(0, r"C:\Users\61422\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.7_qbz5n2kfra8p0\LocalCache\local-packages\Python37\site-packages")#temporarily add library to PATH
sys.path.insert(0, r"C:\Users\61422\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.7_qbz5n2kfra8p0\LocalCache\local-packages\Python37\Scripts")

from bs4 import BeautifulSoup#storing data
import requests
import selenium#inputting data
from selenium import webdriver



page = requests.get("https://www.fuelwatch.wa.gov.au/fuelwatch/pages/home.jspx?rvn=1")
soup = BeautifulSoup(page.content, "html.parser")#getting fuelwatch for data

browser = webdriver.Chrome()
browser.implicitly_wait(10)#waits for all html data to load in

browser.get('https://www.fuelwatch.wa.gov.au/fuelwatch/pages/home.jspx?rvn=1')#getting fuelwatch for input
id_box = browser.find_element_by_id("searchform:location")#finding id of seach bar

id_box.send_keys("WANNEROO")#typing wanneroo for location

button = browser.find_element_by_id("searchform:search")
button.click()#clicks search

browser.implicitly_wait(10)#waits for all html data to load in
table = soup.find(class_="iceDatTbl fw-table")
all_prices = soup.find_all(class_="iceOutTxt")
price = all_prices.find(id='searchResultForm:prices:0:j_id149')
print (price)
x = 1
prices = []
#for i in range (12):
 #   y = str(x)
  #  search_area = "searchResultForm:prices:"+y+":j_id155"
   # price = table[0].find(id="searchResultForm:prices:0:j_id155")
    #prices += price
    #x += 1

print (prices)
#input() so website dosn't close