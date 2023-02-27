# Defines functions to scrape data from Bovada

import bs4
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_bets():
    url = 'https://www.bovada.lv/sports/table-tennis/czech-republic/tt-star-series'
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(executable_path="/Applications/chromedriver_mac64/chromedriver", options=options)
    browser.get(url)
    time.sleep(3)
    html = browser.page_source
    browser.quit()
    soup = bs4.BeautifulSoup(html, 'lxml')
    tags = soup.select(".name")
    names = []
    for tag in tags:
        names.append(tag.text)
    tags = soup.select(".bet-price")
    money_lines = []
    for tag in tags:
        money_lines.append(tag.text)
    return names, money_lines

names, spreads = get_bets()

def only_money_lines(spreads):
    money_lines = []
    for spread in spreads:
        money_line = spread.strip()
        if money_line[0] != '(':
            money_lines.append(money_line)
    return money_lines

print(only_money_lines(spreads))
