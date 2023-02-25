# Defines functions to compare the money line from different websites 
# {team1-team2: [MoneyLine1, MoneyLine2], mets-giants: [+200, -150]}

def find_same_bets(games1, games2):
	"""
	Find the same game from different websites 

	:param: games1: the names of the games from the first website 
	:param: games2: the names of the games from the second website  
	:return: the name of the games that are the same
	"""
	same_games = set(games1) & set(games2)
	same_games = list(same_games)
	return same_games

def find_different_underdog(same_game_keys, games1, games2):
	"""
	Calculates the payout for American odds

	:param: same_game_keys: all of the games that are the same on too different 
			websites
	:param: games1: the dict of all of the games from the first website 
	:param: games2: the dict of all of the games from the second website 
	:return: a dict that contains the games that have different underdogs
	"""
	# bovada = {"mets-giants": [+200, -150], "padres-blue_jays": [+150, -100]}
    # betonline = {"cardinals-yankees": [-150, +100], "mets-giants": [-200, +150]}
	# form of the return dict:
	# {bovada-betonline: ["mets-giants", [+200, -150], [-200, +150]]}
	arb_games = [[None, None, None]]
	new_dct = {"bovada-betonline": arb_games}
	for game in same_game_keys:
		odds1 = games1[game]
		odds2 = games2[game]
		if (odds1[0] > 0 and odds2[0] < 0) or (odds1[0] < 0 and odds2[0] > 0):
			if arb_games == [[None, None, None]]:
				arb_games[0] = [game, odds1, odds2]
			else:
				arb_games.append([game, odds1, odds2])
	return new_dct