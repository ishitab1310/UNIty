import sqlite3
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

# Connect to the SQLite database
conn = sqlite3.connect('players.db')
c = conn.cursor()

# Remove stopwords from the given question
def remove_stopwords(question):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(question)
    filtered_question = [word for word in word_tokens if word.casefold() not in stop_words]
    return ' '.join(filtered_question)

# Search the database for relevant information based on keywords
def search_database(keywords):
    query = f"SELECT * FROM players WHERE data LIKE '%{keywords}%'"
    c.execute(query)
    results = c.fetchall()
    return results

# Extract the specific information from player's data
def extract_information(player_data, field):
    if field in player_data:
        return player_data[field]
    else:
        return "Information not found."

# Run the chatbot
def run_chatbot():
    print("Hi! I'm the Badminton Info Chatbot. How can I help you today?")
    while True:
        question = input("> ")
        if question.lower() == 'quit':
            break
        keywords = remove_stopwords(question)
        results = search_database(keywords)
        if len(results) == 0:
            print("Sorry, I couldn't find any information about that player.")
        elif len(results) == 1:
            player_data = eval(results[0][2])
            print(f"Name: {results[0][1]}")
            for field in player_data:
                if field == 'Name' or field == 'Data':
                    continue
                print(f"{field}: {extract_information(player_data, field)}")
        else:
            print(f"I found {len(results)} players. Which one are you asking about?")
            for i, player in enumerate(results):
                print(f"{i+1}. {player[1]}")
            selection = input("> ")
            try:
                player_data = eval(results[int(selection)-1][2])
                print(f"Name: {results[int(selection)-1][1]}")
                for field in player_data:
                    if field == 'Name' or field == 'Data':
                        continue
                    print(f"{field}: {extract_information(player_data, field)}")
            except (ValueError, IndexError):
                print("Invalid selection.")
                continue

run_chatbot()
