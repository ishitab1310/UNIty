import sqlite3

class DBclass:
    def __init__(self, path):
        self.path = path
        self.db = sqlite3.connect(self.path)
        self.cur = self.db.cursor()
        
    def execute(self, query):
        self.cur.execute(query)
        return [i[0] for i in self.cur.description], self.cur.fetchall()

# Create a DBclass object for the 'players.db' database
db = DBclass('players.db')

# Define a set of rules for the chatbot
rules = {
    'greet': {
        'keywords': ['hello', 'hi', 'hey', 'yo'],
        'response': 'Hi there! How can I help you today?'
    },
    'goodbye': {
        'keywords': ['bye', 'goodbye'],
        'response': 'Goodbye!'
    },
    'player_info': {
        'keywords': ['info'],
        'response': 'Here is the information for {name}:',
        'query': "SELECT * FROM playertables WHERE Name == {name}"
    },
    'list_players': {
        'keywords': ['list players'],
        'response': 'Here are the names of all the players:',
        'query': 'SELECT Name FROM playertables'
    },
    'help': {
        'keywords': ['help'],
        'response': "You can ask for information about a player by saying 'info for {name}', or you can ask for a list of players by saying 'list players'.",
    }
}

# Modify the process_input function to return the bot's response
def process_input(input_text):
    for rule in rules.values():
        for keyword in rule['keywords']:
            if keyword in input_text.lower():
                if rule.get('query'):
                    columns, result = db.execute(rule['query'].format(name=input_text.split()[-1]))
                    if len(result) == 0:
                        return "I'm sorry, I couldn't find any players with that name."
                    output = result
                    if rule['response']:
                        response = rule['response'].format(name=input_text.split()[-1])
                        return response + '\n' + '\n'.join(['\t'.join(map(str, row)) for row in output])
                    else:
                        return '\n'.join(['\t'.join(map(str, row)) for row in output])
                else:
                    return rule['response']
    return "I'm sorry, I don't understand. Type 'help' for a list of available commands."


# Define the main loop of the chatbot
while True:
    input_text = input('> ')
    if input_text.lower() in ['exit', 'quit']:
        print('Goodbye!')
        break
    output_text = process_input(input_text)
    print(output_text)
