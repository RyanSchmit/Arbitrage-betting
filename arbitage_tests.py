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
                self.assertAlmostEqual(money, 183.33)
    
        def test03_american_to_decimal_odds(self):
                odds = payout.american_to_decimal_odds(-145)
                self.assertEqual(odds, 1.6896551724137931)
    
        def test04_american_to_decimal_odds(self):
                odds = payout.american_to_decimal_odds(+145)
                self.assertEqual(odds, 2.45)

        def test05_calculate_hedge(self):
                bet = payout.calculate_hedge(250, 250)
                self.assertEqual(bet, 71.43)

        def test06_calculate_hedge(self):
                bet = payout.calculate_hedge(350, 250)
                self.assertEqual(bet, 100)

        def test07_calculate_profit(self):
                profit = payout.calculate_profit(100, 100, 350)
                self.assertEqual(profit, 150)

        def test08_calculate_profit(self):
                profit = payout.calculate_profit(25, 17.86, 62.50)
                self.assertEqual(profit, 19.64)

        def test09_find_same_bets(self):
                bovada = ["mets-giants", "padres-cardinals"]
                betonline = ["padres-cardinals", "mets-giants"]
                same_money_lines = compare_money_lines.find_same_bets(bovada, betonline)
                expected = ["padres-cardinals", "mets-giants"]
                self.assertEqual(same_money_lines, expected)
        
        def test10_find_same_bets(self):
                bovada = ["dodger-phillies", "white_sox-blue_jays"]
                betonline = ["padres-cardinals", "mets-giants"]
                same_money_lines = compare_money_lines.find_same_bets(bovada, betonline)
                expected = []
                self.assertEqual(same_money_lines, expected)

        def test11_find_different_underdog(self):
                same_game_keys = ["mets-giants"]
                bovada = {"mets-giants": [+200, -150], "padres-blue_jays": [+150, -100]}
                betonline = {"cardinals-yankees": [-150, +100], "mets-giants": [-200, +150]}
                different_underdog = compare_money_lines.find_different_underdog(same_game_keys, bovada, betonline)
                expected = {"bovada-betonline": ["mets-giants", [+200,-150], [-200, +150]]}
                self.assertDictEqual(different_underdog, expected)

        def test12_find_different_underdog(self):
                same_game_keys = ["mets-giants"]
                bovada = {"mets-giants": [+200, -150], "padres-blue_jays": [+150, -100]}
                betonline = {"cardinals-yankees": [-150, +100], "mets-giants": [+220, -140]}
                different_underdog = compare_money_lines.find_different_underdog(same_game_keys, bovada, betonline)
                expected = {"bovada-betonline": [None, None, None]}
                self.assertDictEqual(different_underdog, expected)

        def test13_find_different_underdog(self):
                same_game_keys = ["mets-giants"]
                bovada = {"mets-giants": [+200, -150], "cardinals-yankees": [+150, -100]}
                betonline = {"cardinals-yankees": [-150, +100], "mets-giants": [-200, +150]}
                different_underdog = compare_money_lines.find_different_underdog(same_game_keys, bovada, betonline)
                expected = {"bovada-betonline": [["mets-giants", [+200,-150], [-200, +150]], ["cardinals-yankees", [+150, -100], [-150, +100]]]}
                self.assertDictEqual(different_underdog, expected)

if __name__ == "__main__":
        unittest.main()
 
        