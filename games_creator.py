# Defines function to parse arrays of betting data

# Major sports (don't scrape): soccer, basketball, baseball, football, rugby, 
# tennis, hockey, horse racing, politics
# Only scrape data from non-major sports including: soccer, tennis,
# e-sports, basketball, rugby, table tennis 

# Start with the websites Bovada and My Bookie 
# import get_bovada
# import get_my_bookie

# Class for each game:
# team1: the first team in the alphabet order
# team2: the second team in the alphabet order
# odd1: the money line for the first team 
# odd2: the money line for the second team 
class Game:
    def __init__(self, team1, team2, odd1, odd2):
        self.team1 = team1
        self.team2 = team2
        self.odd1 = odd1
        self.odd2 = odd2

    def __repr__(self):
        return "The game is %s (%d) vs. %s (%d)" % (self.team1, self.odd1, self.team2, self.odd2)

    def __eq__(self, other):
        if type(other) == Game:
            team1Found = (self.team1 == other.team1) or (self.team1 == other.team2)
            team2Found = (self.team2 == other.team2) or (self.team2 == other.team1)
            return (type(other) == Game) and (team1Found and team2Found)
        elif type(other) == str:
            otherTeams = other.split("-")
            team1Found = (self.team1 == otherTeams[0]) or (self.team1 == otherTeams[1])
            team2Found = (self.team2 == otherTeams[1]) or (self.team2 == otherTeams[1])
            return (type(other) == Game) and (team1Found and team2Found)
        else:
            raise TypeError


def create_games(names, money_lines):
    """
    Create classes of all available money lines games for each website 

    :param: names: the array of names of teams scraped from a website 
    :param: money_lines: the array of money lines scraped from a website
    :return: the classes for the games for a website
    """ 
    games = []
    for x in range(len(names)):
        if x % 2 == 0:
            team1 = snake_case(names[x])
            team2 = snake_case(names[x+1])
            odd1 = int(money_lines[x])
            odd2 = int(money_lines[x+1])
            game = Game(team1, team2, odd1, odd2)
            games.append(game)
    return games


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



