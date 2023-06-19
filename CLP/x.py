import string
from flask import Flask, render_template, request
import sqlite3
import stanza
import datetime
# import fasttext 

app = Flask(__name__)

class DBclass:
    def __init__(self, path):
        self.path = path
        
    def execute(self, query):
        db = sqlite3.connect(self.path)
        cur = db.cursor()
        cur.execute(query)
        result = [i[0] for i in cur.description], cur.fetchall()
        db.close()
        return result


with open('stopwords.txt', 'r') as f:
    stopwords = f.read().splitlines()
    
rules = {
    'greet': {
        'keywords': ['hello', 'hi', 'hey', 'yo'],
        'response': 'Hi there! How can I help you today?'
    },
    'goodbye': {
        'keywords': ['bye', 'goodbye','Goodbye','Bye'],
        'response': 'Goodbye!'
    },
    'list_players_by_coach': {
        'keywords': ['teacher', 'coach','coached','mentor'],
        'response': 'Coach of {name} is',
        'query': "SELECT Coach FROM playertables WHERE Lastname ='{name}'"
    },
    'list_players': {
        'keywords': ['list players', 'players list', 'all players'],
        'response': 'Here are the names of all the players:',
        'query': 'SELECT Name FROM playertables'
    },
    'list_players_by_country': {
        'keywords': ['country'],
        # 'full': "SELECT Name FROM playertables WHERE Lastname = '{name}'"
        'response':  '',
        'query': "SELECT Country FROM playertables WHERE Lastname = '{name}'"
    },
    'list_players_by_height_range': {
        'keywords': ['height','length','tall'],
        'response': 'Height of {name} is',
        'query': "SELECT Height FROM playertables WHERE Lastname ='{name}'"
    },
    'list_players_by_medals': {
        'keywords': ['medals won', 'medal count','medals','medal'],
        'response': 'Medals won by {name}:',
        'query': "SELECT Medals FROM playertables WHERE Lastname ='{name}'"
    },
    
    'list_players_by_birthdate_range': {
        'keywords': ['birthdate','date birth','dob','DOB','birthyear','zodiac','cry'],
        'response': '{name} first cried on: ',
        'query': "SELECT Birthdate FROM playertables WHERE Lastname ='{name}'"
    },
    'list_players_by_current_ranking': {
        'keywords': ['current'],
        'response': 'Current Ranking of {name} is ',
        'query': "SELECT Current_Ranking FROM playertables WHERE Lastname ='{name}'"
    },
     'list_players_by_highest_ranking': {
        'keywords': ['highest ranking'],
        'response': 'Highest Ranking of {name} is ',
        'query': "SELECT Highest_Ranking FROM playertables WHERE Lastname ='{name}'"
    },
    'list_players_by_career': {
        'keywords': ['wins', 'losses'],
        'response': 'No. of Wins and Losses of {name}: ',
        'query': "SELECT Career FROM playertables WHERE Lastname ='{name}'"
    },
     'list_players_by_earlylife': {
        'keywords': ['life', 'childhood','early','father','mother'],
        'response': '',
        'query': "SELECT Early_Life FROM playertables WHERE Lastname ='{name}'"
    },
     'list_players_by_surname': {
        'keywords': ['surname','name'],
        'response': 'Full name is ',
        'query': "SELECT Name FROM playertables WHERE Firstname ='{name}'"
    },
    'list_players_by_hometown': {
        'keywords': ['hometown','home'],
        'response': '',
        'query': "SELECT Hometown FROM playertables WHERE Lastname ='{name}'"
    },
    'list_players_by_start': {
        'keywords': ['onset','beginning','start'],
        'response': '',
        'query': "SELECT Starting FROM playertables WHERE Lastname ='{name}'"
    },
    'list_players_by_learn': {
        'keywords': ['initial','learning'],
        'response': '',
        'query': "SELECT Learning FROM playertables WHERE Lastname ='{name}'"
    },
    'list_players_by_endo': {
        'keywords': ['sponsorship','endorsement'],
        'response': '',
        'query': "SELECT Endorsements FROM playertables WHERE Lastname ='{name}'"
    },
    'list_players_by_achievements': {
        'keywords': ['reward','achieve','title','achievement','rewards','achievements'],
        'response': '',
        'query': "SELECT Achievements FROM playertables WHERE Lastname ='{name}'"
    },
    'help': {
        'keywords': ['help'],
        'response': "You can ask for information about a player by saying 'info for {last_name}', 'tell me about {last_name}', 'who is {last_name}', or 'details of {last_name}'. "
                    "You can also get a list of all players by saying 'list players', or get specific lists of players based on different criteria."
                    "Make sure to add last name of the required player at the end of every question you ask."
                    "You can ask for informtion like: country, height, career, medals, coach, insight, early life, hometown, endorsements, achievements, highest ranking, etc. "
        
    },
    'player_info': {
        'keywords': ['info', 'details','information'],
        'response': 'Here is the information for {name}:',
        'query': "SELECT Insight FROM playertables WHERE Lastname = '{name}'"
    }
}

nlp = stanza.Pipeline(lang='en', processors='tokenize,pos')
# model = fasttext.load_model('/Users/udaybindal/Library/Caches/pip/wheels/64/57/bc/1741406019061d5664914b070bd3e71f6244648732bc96109e/fasttext-0.9.2-cp39-cp39-macosx_13_0_universal2.whl')


def process_input(input_text, db):
    wordafterchecking =""
    input_text = input_text.lower()
    input_text = input_text.translate(str.maketrans('', '', string.punctuation))
    # print(input_text)
    words = input_text.split()
    words = [wording for wording in words if wording not in stopwords]
    # word_vectors = [model.get_word_vector(word) for word in words]
    # word_vectors_text = [' '.join(map(str, vector)) for vector in word_vectors]
    print(len(words))
    for i in range(len(words)):
        wordafterchecking = wordafterchecking + " " + words[i]
    
    
        
    # print(wordafterchecking)
    doc = nlp(wordafterchecking)
    
    user_input_tokens = [(word.text, word.upos) for sent in doc.sentences for word in sent.words]
    max_match =0
    # best_match = None
    best_keyword = None
    for rule in rules.values():
        for keyword in rule['keywords']:
            doc2 = nlp(keyword)
            keyword_tokens = [(word.text, word.upos) for sent in doc2.sentences for word in sent.words]
            # keyword_pos_tags = [(token, "") for token in keyword_tokens]
            print(keyword_tokens)
            # print(keyword_pos_tags)
            # print(len(keyword_tokens))
            print(user_input_tokens)
            # print(len(user_input_tokens))
            # for t in user_input_tokens:
            #     for k in keyword
            # if all(tag in user_input_tokens for tag in keyword_pos_tags):
            #     if best_match is None or len(keyword_pos_tags) > len(best_match):
            #         best_match = keyword_pos_tags
            #         best_keyword = keyword
            matches = sum(1 for token in user_input_tokens if token[1] in [kw_token[1] for kw_token in keyword_tokens])
            print("matches = ",matches)
            exists=0
            for i in user_input_tokens[0]:
                if keyword == i:
                    exists = 1
            if exists == 0:
                matches = 0
                
            if matches > max_match:
                max_match = matches
                best_keyword = keyword
            print(best_keyword)
            print("max = ",max_match)
            
            # if len(keyword_tokens) != len(user_input_tokens):
            #     continue
            
            # matches = all(token[1] == keyword_tokens[i] for i, token in enumerate(user_input_tokens))
    if max_match:
        
        for rule in rules.values():
            for keyword in rule['keywords']:
                # print(keyword)
                if keyword == best_keyword:
                    if rule.get('query'):
                        print(rule)
                        print(wordafterchecking)
                        columns, result = db.execute(rule['query'].format(name=wordafterchecking.split()[-1]))
                        print("result=",len(result))
                        print(result)
                        if len(result) == 0:
                            return "I'm sorry, I couldn't find any players with that name."
                        output = result
                        if rule['response']:
                            response = rule['response'].format(name=wordafterchecking.split()[-1])
                            return response + '\n' + '\n'.join(['\t'.join(map(str, row)) for row in output])
                        else:
                            return '\n'.join(['\t'.join(map(str, row)) for row in output])
                    else:
                        return rule['response']
        return "I'm sorry, I don't understand. Type 'help' for a list of available commands."
    else:
        nothing = {
            'here':{
                'query' :  "SELECT Lastname FROM playertables" 
            }        
        }
        x = nothing['here']
        columns,y = db.execute(x['query'])
        print(y)
        
        z = wordafterchecking.split()[-1]
        print(z.lower())
        # print(y[0][0],y[1],y[2])
        for i in range(len(y)):
            if z.lower() == y[i][0]:
                rule = rules['player_info']
                columns,result = db.execute(rule['query'].format(name=wordafterchecking.split()[-1]))
                output = result
                if rule['response']:
                        response = rule['response'].format(name=wordafterchecking.split()[-1])
                        return response + '\n' + '\n'.join(['\t'.join(map(str, row)) for row in output])
        # print(result)
        return "I'm sorry, I don't understand. Type 'help' for a list of available commands."

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/process_input', methods=['POST'])
def process_input_route():
    
    nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos')
    db = DBclass('players.db')
    current_time = datetime.datetime.now().time()
    # start_time = datetime.time(22, 0)  # 10 PM
    # end_time = datetime.time(3, 0)  # 5 AM

    # if start_time <= current_time or current_time <= end_time:
    #     bot_response = "Go back and study # YOU ARE IN IIIT"
    #     return bot_response
    
    # else:
    #     message = "Welcome to the chat! How can I assist you today?"

    user_input = request.form['input_text']
    bot_response = process_input(user_input, db)
    
    return bot_response

if __name__ == '__main__':
    app.run(port= 8000)