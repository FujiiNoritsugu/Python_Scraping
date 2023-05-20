from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import time
from selenium.webdriver.common.by import By
from openpyxl Workbook


option = Options()
option.add_argument('--headless')

driver = webdriver.Chrome(options=option)
driver.get('https://www.google.co.jp/')

# 検索フィールドの取得
query = driver.find_element(by=By.NAME, value='q')

# 検索文字列を入力
query.send_keys('k4sen')

# 3秒待つ
time.sleep(3)

# 検索ボタンをクリック
button = driver.find_element(by=By.NAME, value='btnK')
button.click()

# 3秒待つ
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

wb = Workbook()

ws = wb.active

ll = [x for x in soup.text.split(' ') if len(x) > 0]
i = 1
for elem in ll:
    ws["A" + i] = elem
    print(i)
    print(elem)
    i+=1
wb.save('result.xlsx')

