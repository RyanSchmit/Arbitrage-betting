# Defines function to scrape a website for the money lines 

# Major sports (don't scrape): soccer, basketball, baseball, football, rugby, 
# tennis, hockey, horse racing, politics

# Only scrape data from non-major sports including: soccer, tennis,
# e-sports, basketball, rugby 

from urllib.request import urlopen

def scrape_page(url):
	"""
	Parse the website 

	:param: url: the url of the website to parse 
	:return: the html og a url  
	"""
	url = "https://sportsbook.fanduel.com/soccer"
	page = urlopen(url)
	print(page)
	html_bytes = page.read()
	html = html_bytes.decode("utf-8")
	print(html)

def extract_money_lines(html):
	"""
	Parse the html

	:param: html: the html of a webpage
	:return: the money lines 
	"""


# Money line dict form:
# {Team1-Team2: [MoneyLine1, MoneyLine2], Mets-Giants: [+200, -150]}
def create_money_lines_dict(money_lines):
	"""
	Parse the money lines

	:param: money lines: the raw money lines from the html 
	:return: the money lines dict 
	"""

def team_swap(team1, team2, line1, line2):
	"""
	Swap the teams if needed

	:param: team1: the name of first team
	:param: team2: the name of the second team 
	:param: line1: the money line for team 1 
	:param: line2: the money line for team 2
	:return: the money line dict with teams in alphabetical order 
	         with matching money lines
	"""

def snake_case(string):
    """
    Replace all spaces in a string with underscores and lowercase all letters.
    TODO: Complete this function. It must use a "for" loop.
    :param string: A string to be snake-cased
    :return: The snake-cased string
    """
    newString = ''
   
    for c in string:
        if c == ' ':
           newString += '_'
        elif type(c) == str:
           newString += c.lower()
        else:
           newString += c 
    return newString

	
