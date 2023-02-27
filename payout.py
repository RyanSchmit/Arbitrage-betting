# Defines function to calculate the payout and 

def calculate_payout(odds, bet):
	"""
	Calculates the payout for American odds

	:param: odds: the American odds for a certain bet 
	:param: bet: how much money was put down a bet
	:return: the payout 
	"""
	if odds > 0:
		payout = (1 + (odds/100)) * bet
		payout = round(payout, 2)
		return payout
	elif odds < 0:
		payout = (1 - (100/odds)) * bet
		payout = round(payout, 2)
		return payout
	return None 

def american_to_decimal_odds(am_odds):
	"""
	Calculates the decimal odds given the American odds

	:param: am_odds: the positive American odds for a certain bet 
	:return: the decimal odds  
	"""
	if am_odds > 0:
		decimal_odds = 1 + (am_odds/100)
		return decimal_odds
	elif am_odds < 0:
		decimal_odds = 1 - (100/am_odds)
		return decimal_odds
	return None 


def calculate_hedge(payout, odds):
	"""
	Calculate how much to put to the second bet to hedge your first 

	:param: payout: the expected payout of the first bet 
	:param: odds: positive American odds for the second bet
	:return: the how much to put to the second bet
	"""
	if odds > 0:
		hedge = payout/(1 + (odds/100))
		hedge = round(hedge, 2)
		return hedge
	elif odds < 0:
		hedge = payout/((100/odds) + 1)
		hedge = round(hedge, 2)
		return hedge
	return None 

def calculate_profit(bet1, bet2, payout):
	"""
	Calculate the profit

	:param: bet1: how much money will be put into the first bet 
	:param: bet2: how much money will be put into the second bet 
	:param: payout1: the payout of the each bet (should be equal)
	:return: the profit 
	"""
	profit = payout - (bet1 + bet2) 
	return profit 
