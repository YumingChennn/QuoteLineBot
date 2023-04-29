#載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#設定 Chorme Driver 的執行檔路徑
options=Options()
options.chrome_executable_path= "/chromedriver_mac_arm64/chromedriver"
# 建立 Driver 物件實體，用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://www.google.com/")
driver.save_screenshot("screenshot.google.png")
driver.close()