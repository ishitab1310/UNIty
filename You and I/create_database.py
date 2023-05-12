import sqlite3

def create_players_table():
    conn = sqlite3.connect('players.db')
    c = conn.cursor()

    # Create the players table
    c.execute('''CREATE TABLE IF NOT EXISTS players (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    description TEXT,
                    data TEXT
                )''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_players_table()
