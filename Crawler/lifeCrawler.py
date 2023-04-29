import os
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.chrome_executable_path=r"C:\Users\Ken Chen\PycharmProjects\LineBot\chromedriver.exe"

driver = webdriver.Chrome(options=options)
driver.get("https://www.brainyquote.com/")
driver.get("https://www.brainyquote.com/topics/life-quotes")

quoteList = []
authorList = []

for i in range(17):
    quotes = driver.find_elements(By.CSS_SELECTOR, '[style="display: flex;justify-content: space-between"]')
    for quote in quotes:
        quoteList.append(quote.text)
    #print(quoteList)
    authors = driver.find_elements(By.CSS_SELECTOR, '[title="view author"]')
    for author in authors:
        authorList.append(author.text)

    # 滾動到頁面底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 取得下一頁
    try:
        link = driver.find_element(By.LINK_TEXT,"Next")
    except:
        print("Can't find the next button.")
        break

    #模擬使用者點擊連結
    driver.execute_script("arguments[0].click();", link)

pqCombine = list(zip(quoteList,authorList))
print(pqCombine)
driver.close()

directory = '/Users/kenchen/PycharmProjects/Selenium/quoteCrawler'
if not os.path.exists(directory):
    os.makedirs(directory)

filename = 'lifeQuo.pkl'
filepath = os.path.join(directory, filename)


# 將list保存為pickle檔案
with open(filepath,'wb') as f:
    pickle.dump(pqCombine,f)