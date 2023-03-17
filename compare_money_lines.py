# Defines functions to compare the money line from different websites 
# Change to check for each team having different odds
import payout

def find_same_bets(games1, games2):
	"""
	Find the same game from different websites 

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
	common_games = {}
	for key in keys:
		type_of = type(seen_games[key])
		if type_of == list:
			common_games[key] = seen_games[key]
	return common_games

def arbitrage_opportunity(game1, game2):
	"""
	Decide if a game is an arbitrage opportunity or not 
	:param: game1: the money line on one website
	:param: game2: the money line on a different website
	:return: if the game is an arbitrage opportunity or not 
	"""
	# Website one analysis 
	underdog1 = 0
	if game1.odd1 < 0 and game1.odd2 < 0:
		return "No, because there isn't any underdog on either or both websites."
	elif game1.odd1 > 0:
		underdog1 = game1.team1
	elif game1.odd2 > 0:
		underdog1 = game1.team2

	# Website two analysis 
	underdog2 = 0
	if game2.odd1 < 0 and game2.odd2 < 0:
		return "No, because there isn't any underdog on either or both websites."
	elif game2.odd1 > 0:
		underdog2 = game2.team1
	elif game2.odd2 > 0:
		underdog2 = game2.team2


	# Check game underdog
	if underdog1 == underdog2:
		return 'No, because the underdog is the same.'
	else:
		return "Possible arbitrage"
