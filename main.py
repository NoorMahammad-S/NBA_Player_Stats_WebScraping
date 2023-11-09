import requests
from bs4 import BeautifulSoup
import csv

# URL of the website containing NBA player stats
url = "https://www.basketball-reference.com/leagues/NBA_2021_per_game.html"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing player statistics
table = soup.find('table', {'id': 'per_game_stats'})

# Create a CSV file to store the scraped data
csv_filename = "nba_player_stats_2021.csv"

# Open the CSV file for writing with UTF-8 encoding
with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    # Find and write the header row
    header = [th.text for th in table.thead.findAll('th')]
    writer.writerow(header)

    # Find and write data rows
    rows = table.tbody.findAll('tr')
    for row in rows:
        data = [td.text for td in row.findAll('td')]
        writer.writerow(data)

print(f"Scraped NBA player stats and saved to {csv_filename}")
