import unittest
import payout
import compare_money_lines
import games_creator

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
        
        def test09_snake_case(self):
                string = games_creator.snake_case("Blue Jays")
                self.assertEqual(string, "blue_jays")
        
        def test10_snake_case(self):
                string = games_creator.snake_case("12343143241234 Ryan bob John Mic miKe Bob")
                self.assertEqual(string, "12343143241234_ryan_bob_john_mic_mike_bob")

        def test11_create_money_lines_dict(self):
                names = ['Richmond Tigers', 'Carlton Blues', 'Geelong Cats', 'Collingwood Magpies']
                money_lines = ['-150', '+115', '-205', '+155']
                expected = [games_creator.Game('richmond_tigers', 'carlton_blues', -150, 115), games_creator.Game('geelong_cats', 'collingwood_magpies', -205, +155)]
                games = games_creator.create_games(names, money_lines)
                self.assertEqual(games, expected)

        def test12_find_same_bets(self):
                bovada = [games_creator.Game('richmond_tigers', 'carlton_blues', -150, 115), games_creator.Game('geelong_cats', 'collingwood_magpies', -205, +155)]
                my_bookie = [games_creator.Game('geelong_cats', 'collingwood_magpies', -150, +155)]
                expected = {'collingwood_magpies/geelong_cats': [games_creator.Game('geelong_cats', 'collingwood_magpies', -205, +155), games_creator.Game('geelong_cats', 'collingwood_magpies', -150, +155)]}
                common_games = compare_money_lines.find_same_bets(bovada, my_bookie)
                self.assertEqual(common_games, expected)

if __name__ == "__main__":
        unittest.main()
 
        