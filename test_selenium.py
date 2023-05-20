from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

# 変更点1: 検索文字を設定
search_word = "自分の好きな言葉"

option = Options()
option.add_argument('--headless')

driver = webdriver.Chrome(options=option)
driver.get('https://www.google.co.jp/')

# 変更点2: 検索ボックスに検索文字を入力
search_box = driver.find_element_by_name('q')
search_box.send_keys(search_word)
search_box.submit()

# 検索結果の表示待ち（任意の秒数を指定）
driver.implicitly_wait(5)

# 変更点3: 検索結果の一覧からランダムにリンクを選択
links = driver.find_elements_by_css_selector('div.r a')
if links:
    # 最初のリンクを選択
    links[0].click()

    # 変更点4: 表示されたページのテキストを取得し、検索文字の出現回数をカウント
    page_html = driver.page_source
    page_soup = BeautifulSoup(page_html, 'html.parser')
    page_text = page_soup.get_text()
    word_count = page_text.count(search_word)

    # 出力
    print(f"検索文字 '{search_word}' の出現回数: {word_count}")
else:
    print("検索結果が見つかりませんでした。")

# ブラウザを終了
driver.quit()
