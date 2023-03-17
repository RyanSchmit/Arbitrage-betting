# Defines functions to scrape data from My Bookie
# Change the class names for different sports

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
    url = 'https://www.mybookie.ag/sportsbook'
    if sport == 'table tennis':
        url = url + '/table-tennis'
    # Get all esports instead of just Call of Duty
    if sport == 'esports':
         url = url + '/call-of-duty/#accordionBets1809'
    if sport == 'australian-football':
         url = url + '/australian-football/'
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
    """
    Gets just the money lines from the text 
    :param: spread: the array of data taken from the money_lines class (css)
    :return: money_lines: an array with just the money lines
    """
    money_lines = []
    for spread in spreads:
        if spread != None:
            money_lines.append(spread.text)
    return money_lines

def only_names(names_data):
    """
    Gets just the names from the text 
    :param: names_data: the array of data taken from the names class (css)
    :return: names: an array with just the names
    """
    names = []
    
    for x in names_data:
        found = x.find("vs.")
        # if found != -1:
        #     dash_point = (x.find("-")) + 1
        #     just_teams_str = x[dash_point:]
        #     just_teams_str = just_teams_str.split("vs.")
        #     for team in just_teams_str:
        #         team = team.strip()
        #         names.append(team)
        # else:
        #     team = x.strip()
        #     names.append(team)
        team = x.strip()
        names.append(team)
    return names


def get_bets(html):
    """
    Extract names of teams and money lines from html
    :param: html: the raw html
    :return: array of the names of the teams and array of 
    corresponding money lines
    """
    tags_vis = html.select(".game-line__visitor-team__name" + ".m-0")
    tags_home = html.select(".game-line__home-team__name" + ".m-0")
    names = []
    for tag in range(len(tags_vis)):
        names.append(tags_vis[tag].text)
        names.append(tags_home[tag].text)
    tags = html.select(".lines-odds")
    money_lines = []
    for tag in tags:
        money_lines.append(tag.span)
    money_lines = only_money_lines(money_lines)
    names = only_names(names)
    # if len(names) == len(money_lines):
    #     return names, money_lines
    # Check if money line is empty
    # elif len(money_lines) > len(names):
    # money_lines = money_lines[:(len(names) - 2)]
    # names = names[:(len(money_lines) - 2)]
    return names, money_lines
    # else:
        # Remove the extra money lines
        # raise Exception("Teams and money lines are not matching", money_lines)
# html = get_html("australian-football")
# names, money_lines = get_bets(html)
# print(names, money_lines)

