import requests
from bs4 import BeautifulSoup
import re

def scrape_player_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract player information from the individual page
    name = soup.find("h1", class_="firstHeading").text.strip()
    description = soup.find("div", class_="mw-parser-output").p.text.strip()

    player_info_table = soup.find("table", class_="infobox vcard")
    rows = player_info_table.find_all("tr")

    data = {}
    for row in rows:
        header = row.find("th")
        if header:
            field = header.text.strip()
            if field.endswith(":"):
                field = field[:-1]

            value = row.find("td")
            if value:
                value = value.text.strip()
                data[field] = value

    # Update the extracted player data into a dictionary
    player = {
        "name": name,
        "description": description,
        "data": data
    }

    return player

def scrape_players():
    player_urls = [
        "https://en.wikipedia.org/wiki/P._V._Sindhu",
        "https://en.wikipedia.org/wiki/Pullela_Gopichand",
        "https://en.wikipedia.org/wiki/Saina_Nehwal",
        "https://en.wikipedia.org/wiki/Srikanth_Kidambi",
        "https://en.wikipedia.org/wiki/Prakash_Padukone",
        "https://en.wikipedia.org/wiki/Parupalli_Kashyap",
        "https://en.wikipedia.org/wiki/Jwala_Gutta",
        "https://en.wikipedia.org/wiki/Ashwini_Ponnappa",
        "https://en.wikipedia.org/wiki/B._Sai_Praneeth",
        "https://en.wikipedia.org/wiki/Chirag_Shetty"
    ]

    players = []
    for url in player_urls:
        player_data = scrape_player_data(url)
        players.append(player_data)

    return players

if __name__ == '__main__':
    player_data = scrape_players()
    for player in player_data:
        print(player)
