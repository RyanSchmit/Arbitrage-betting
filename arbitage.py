# Looks at two websites to find the arbitrage bets available  
import get_bovada
import games_creator
import get_my_bookie
import compare_money_lines

def main():
	html = get_bovada.get_html("australian-football")
	bovada_names, bovada_money_lines = get_bovada.get_bets(html)
	bovada_games = games_creator.create_games(bovada_names, bovada_money_lines)

	html = get_my_bookie.get_html("australian-football")
	my_bookie_names, my_bookie_money_lines = get_my_bookie.get_bets(html)
	my_bookie_games = games_creator.create_games(my_bookie_names, my_bookie_money_lines)
		
	same_teams = compare_money_lines.find_same_bets(bovada_games, my_bookie_games)
	keys = same_teams.keys()
	for key in keys:
		print(same_teams[key])

if __name__ == "__main__":
	main()

# {'collingwood_magpies/geelong_cats': [The game is geelong_cats (-190) vs. collingwood_magpies (145), The game is collingwood_magpies (143) vs. geelong_cats (-200)], 'brisbane_lions/port_adelaide_power': [The game is port_adelaide_power (-110) vs. brisbane_lions (-120), The game is brisbane_lions (-133) vs. port_adelaide_power (-116)], 'melbourne_demons/western_bulldogs': [The game is melbourne_demons (-170) vs. western_bulldogs (130), The game is western_bulldogs (101) vs. melbourne_demons (-158)], 'gold_coast_suns/sydney_swans': [The game is gold_coast_suns (130) vs. sydney_swans (-170), The game is sydney_swans (-175) vs. gold_coast_suns (112)], 'adelaide_crows/gws_giants': [The game is gws_giants (-155) vs. adelaide_crows (120), The game is adelaide_crows (114) vs. gws_giants (-181)], 'essendon_bombers/hawthorn_hawks': [The game is hawthorn_hawks (135) vs. essendon_bombers (-175), The game is essendon_bombers (-185) vs. hawthorn_hawks (116)]}