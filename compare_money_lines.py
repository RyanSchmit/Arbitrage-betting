# Defines functions to compare the money line from different websites 
# Change to check for each team having different odds

def find_same_bets(games1, games2):
	"""
	Find the same team from different websites 

	:param: games1: the names of the games from the first website 
	:param: games2: the names of the games from the second website  
	:return: the name of the games that are several websites and the differing odds
	"""
	seen_games = {}
	for game in games1:
		team1 = game.team1
		team2 = game.team2
		if game.team1 > game.team2:
			team1 = game.team2
			team2 = game.team1
		game_name = team1 + "/" + team2
		if game_name in seen_games:
			current_games = seen_games[game_name]
			new_games = [current_games, game]
			seen_games[game_name] = new_games
		else:
			seen_games[game_name] = game
	
	for game in games2:
		team1 = game.team1
		team2 = game.team2
		if game.team1 > game.team2:
			team1 = game.team2
			team2 = game.team1
		game_name = team1 + "/" + team2
		if game_name in seen_games:
			current_games = seen_games[game_name]
			new_games = [current_games, game]
			seen_games[game_name] = new_games
		else:
			seen_games[game_name] = game
	
	keys = seen_games.keys()
	pos_arbs = {}
	for key in keys:
		type_of = type(seen_games[key])
		if type_of == list:
			pos_arbs[key] = seen_games[key]
	return pos_arbs
