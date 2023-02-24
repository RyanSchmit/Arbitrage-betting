import unittest
import payout
import compare_money_lines
import web_scrape

class TestArbitrage(unittest.TestCase):
    def test01_payout(self):
        money = payout.calculate_payout(+150, 100)
        self.assertEqual(money, 250.00)
        
    def test02_payout(self):
        money = payout.calculate_payout(-120, 100)
        self.assertEqual(money, 183.33)
    
    def test03_american_to_decimal_odds(self):
            odds = payout.american_to_decimal_odds(-145)
            self.assertEqual(odds, 1.6896551724137931)
    
    def test04_american_to_decimal_odds(self):
            odds = payout.american_to_decimal_odds(+145)
            self.assertEqual(odds, 2.45)