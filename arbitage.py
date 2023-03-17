# Looks at two websites to find the arbitrage bets available  
import get_bovada
import games_creator
import get_my_bookie
import compare_money_lines
import payout

def main():
	html = get_bovada.get_html("australian-football")
	bovada_names, bovada_money_lines = get_bovada.get_bets(html)
	bovada_games = games_creator.create_games(bovada_names, bovada_money_lines)

	html = get_my_bookie.get_html("australian-football")
	my_bookie_names, my_bookie_money_lines = get_my_bookie.get_bets(html)
	my_bookie_games = games_creator.create_games(my_bookie_names, my_bookie_money_lines)
		
	same_games = compare_money_lines.find_same_bets(bovada_games, my_bookie_games)
	keys = same_games.keys()
	# add to different keys variable
	for key in keys:
		result = compare_money_lines.arbitrage_opportunity(same_games[key][0], same_games[key][1])
		print(key + ": " + result)
		
	# print(same_games[])
	# for key in keys:
	# 	games = same_games[key]
	# 	payout1 = 0
	# 	payout2 = 0
	# 	hedge = 0
	# 	if games[0].odd1 > 0:
	# 		payout1 = payout.calculate_payout(games[0].odd1, 100)
	# 		print("You would get a payout of " + str(payout1) + " by putting " + "$100 on " + games[0].team1)
	# 	else:
	# 		payout1 = payout.calculate_payout(games[0].odd2, 100)
	# 		print("You would get a payout of " + str(payout1) + " by putting " + "$100 on " + games[0].team2)
	# 	if games[1].odd1 > 0:
	# 		hedge = payout.calculate_hedge(payout1, games[1].odd1)
	# 		print("You should put " + str(hedge) + " on " + games[1].team1)
	# 		payout2 = payout.calculate_payout(games[1].odd1, hedge)
	# 		print("You would get a payout of " + str(payout2) + " by putting " + str(hedge) + " on " + games[1].team1)
	# 	else:
	# 		hedge = payout.calculate_hedge(payout1, games[1].odd2)
	# 		print("You should put " + str(hedge) + " on " + games[1].team2)
	# 		payout2 = payout.calculate_payout(games[1].odd2, hedge)
	# 		print("You would get a payout of " + str(payout2) + " by putting " + str(hedge) + " on " + games[1].team2)
	# 	profit = payout.calculate_profit(100, hedge, payout1)
	# 	print("The Profit is " + str(profit))
	# 	print("\n")
	
if __name__ == "__main__":
	main()


# {'collingwood_magpies/geelong_cats': [The game is geelong_cats (-190) vs. collingwood_magpies (145), The game is collingwood_magpies (143) vs. geelong_cats (-200)],
