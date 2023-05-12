import sqlite3
from scrape_players import scrape_players

def populate_players_table():
    conn = sqlite3.connect('players.db')
    c = conn.cursor()

    players = scrape_players()

    for player in players:
        name = player['name']
        description = player['description']
        data = str(player['data'])

        c.execute("INSERT INTO players (name, description, data) VALUES (?, ?, ?)",
                  (name, description, data))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    populate_players_table()
