import sys
sys.path.insert(0, r"C:\Users\61422\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.7_qbz5n2kfra8p0\LocalCache\local-packages\Python37\site-packages")#temporarily add modules to PATH
sys.path.insert(0, r"C:\Users\61422\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.7_qbz5n2kfra8p0\LocalCache\local-packages\Python37\Scripts")

from bs4 import BeautifulSoup#storing data
import requests
import selenium#inputting data
from selenium import webdriver




page = requests.get("https://www.google.com/search?q=fishing+memes&safe=strict&rlz=1C1CHBF_en-GBAU866AU866&sxsrf=ACYBGNR25PvVJqY8TmqtMNG4a-LJM2AY_w:1574920444560&source=lnms&tbm=isch&sa=X&ved=2ahUKEwih0Jbtm4zmAhVP8XMBHVzYAlsQ_AUoAXoECAsQAw&biw=1920&bih=975")
soup = BeautifulSoup(page.content, "html.parser")#getting fuelwatch for data

browser = webdriver.Chrome()
browser.implicitly_wait(50)#waits for all html data to load in

browser.get('https://www.google.com/search?q=fishing+memes&safe=strict&rlz=1C1CHBF_en-GBAU866AU866&sxsrf=ACYBGNR25PvVJqY8TmqtMNG4a-LJM2AY_w:1574920444560&source=lnms&tbm=isch&sa=X&ved=2ahUKEwih0Jbtm4zmAhVP8XMBHVzYAlsQ_AUoAXoECAsQAw&biw=1920&bih=975')#getting fuelwatch for input





fishing_memes = []
class_of_pics = soup.find_all(class_="THL2l")
print (class_of_pics)