# Defines functions to scrape data from Bovada

import bs4
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_html(sport):
    """
    Get the raw html for the website
    :param: sport: the sport that you want to get the bets for
    :return: the raw html for a sport
    """
    url = 'https://www.bovada.lv/sports'
    if sport == 'table tennis':
        url = url + '/table-tennis'
    if sport == 'esports':
         url = url + '/esports'
    if sport == 'australian-football':
        url = url + '/aussie-rules'
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(executable_path="/Applications/chromedriver_mac64/chromedriver", options=options)
    browser.get(url)
    time.sleep(3)
    html = browser.page_source
    browser.quit()
    soup = bs4.BeautifulSoup(html, 'lxml')
    return soup

def only_money_lines(spreads):
    money_lines = []
    for spread in spreads:
        money_line = spread.strip()
        if money_line[0] != '(':
            money_lines.append(money_line)
    return money_lines

def get_bets(html):
    """
    Extract names of teams and money lines from html
    :param: html: the raw html
    :return: array of the names of the teams and array of 
    corresponding money lines
    """
    tags = html.select(".name")
    names = []
    for tag in tags:
        names.append(tag.text)
    tags = html.select(".bet-price")
    money_lines = []
    for tag in tags:
        money_lines.append(tag.text)
    money_lines = only_money_lines(money_lines)
    if len(names) == len(money_lines) and (len(names) % 2 == 0):
        return names, money_lines
    else:
        raise Exception("Teams and money lines are not matching")