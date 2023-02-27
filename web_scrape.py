# Defines function to parse raw betting data

# Major sports (don't scrape): soccer, basketball, baseball, football, rugby, 
# tennis, hockey, horse racing, politics

# Only scrape data from non-major sports including: soccer, tennis,
# e-sports, basketball, rugby 

# Start with the websites Bovada and DraftKings 
import getBovadaBets

# Money line dict form:
# {Team1-Team2: [MoneyLine1, MoneyLine2], Mets-Giants: [+200, -150]}
def create_money_lines_dict(names, money_lines):
	"""
	Create dicts of all available money lines for each website 

   :param: names: the array of names of teams scraped from a website 
	:param: money_lines: the array of money lines 
	:return: the money lines dict for a website
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

	
