# Defines functions to compare the money line from different websites 
# {team1-team2: [MoneyLine1, MoneyLine2], mets-giants: [+200, -150]}

def find_same_bets(games1, games2):
	"""
	Find the same game from different websites 

	:param: games1: the names of the games from the first website 
	:param: games2: the names of the games from the second website  
	:return: the name of the games that are the same
	"""
	pass

def find_different_underdog(same_game_keys, games1, games2):
	"""
	Calculates the payout for American odds

	:param: same_game_keys: all of the games that are the same on too different 
			websites
	:param: games1: the dict of all of the games from the first website 
	:param: games2: the dict of all of the games from the second website 
	:return: a dict that contains the games that have different underdogs
	"""
	# form of the return dict:
	# {barstool-fanduel: ["mets-giants", [+200, -150], [-200, +150]]}
	dict = {}
	return dict