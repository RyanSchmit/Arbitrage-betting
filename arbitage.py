# Looks at two websites to find the arbitrage bets available 
import web_scrape

def main():
	urls = ['https://sportsbook.fanduel.com/soccer', 'https://www.barstoolsportsbook.com/sports/football?category=upcoming']
	for url in urls:
		web_scrape.scrape_page(url)
		
if __name__ == "__main__":
	main()