# Looks at two websites to find the arbitrage bets available 
import web_scrape

def main():
	urls = ['https://www.bovada.lv/sports', 'https://www.betonline.ag/sportsbook']
	for url in urls:
		web_scrape.scrape_page(url)
		
if __name__ == "__main__":
	main()