# 🏀 NBA Player Stats Scraper – 2021 Season (Basketball Reference)

Easily scrape comprehensive NBA player statistics from the 2021 season using this Python script. Powered by `requests` and `BeautifulSoup`, this tool pulls player data directly from [Basketball Reference](https://www.basketball-reference.com), processes it, and exports the information into a clean, structured CSV file.

## 📌 Features

* Scrapes real-time NBA player stats from the 2021 season
* Extracts key metrics such as points, assists, rebounds, shooting percentages, and more
* Outputs data to a ready-to-analyze CSV file
* Simple and lightweight, with minimal dependencies

## ✅ Requirements

Make sure Python is installed on your machine. Then install the required libraries:

```bash
pip install requests beautifulsoup4
```

## 🚀 How to Use

1. **Clone or Download** this repository to your local environment.

2. **Navigate to the project directory** using your terminal:

   ```bash
   cd https://github.com/NoorMahammad-S/NBA_Player_Stats_WebScraping.git
   ```

3. **Run the scraper script:**

   ```bash
   python nba_player_stats_scraper.py
   ```

4. The script will fetch NBA player statistics from Basketball Reference and save the data to a file called:

   ```
   nba_player_stats_2021.csv
   ```

## 📊 CSV Output Format

The exported CSV file includes the following columns:

* `Player`: Player Name
* `Pos`: Position
* `Age`: Age
* `Team`: Team
* `G`: Games Played
* `GS`: Games Started
* `MP`: Minutes Played per Game
* `FG`: Field Goals Made per Game
* `FGA`: Field Goals Attempted per Game
* `FG%`: Field Goal Percentage
* `3P`: Three-Point Field Goals Made per Game
* `3PA`: Three-Point Field Goals Attempted per Game
* `3P%`: Three-Point Field Goal Percentage
* `2P`: Two-Point Field Goals Made per Game
* `2PA`: Two-Point Field Goals Attempted per Game
* `2P%`: Two-Point Field Goal Percentage
* `eFG%`: Effective Field Goal Percentage
* `FT`: Free Throws Made per Game
* `FTA`: Free Throws Attempted per Game
* `FT%`: Free Throw Percentage
* `ORB`: Offensive Rebounds per Game
* `DRB`: Defensive Rebounds per Game
* `TRB`: Total Rebounds per Game
* `AST`: Assists per Game
* `STL`: Steals per Game
* `BLK`: Blocks per Game
* `TOV`: Turnovers per Game
* `PF`: Personal Fouls per Game
* `PTS`: Points per Game

## 🛠 Contributing

Want to improve this scraper or add new features? Contributions are welcome! Feel free to fork the project, create a new branch, and submit a pull request. You can also open an issue to report bugs or suggest enhancements.

---

## 📣 Keywords

NBA stats scraper, Basketball Reference scraper, Python web scraping, NBA player data, basketball stats 2021, BeautifulSoup NBA, NBA CSV stats, sports analytics tools

---
