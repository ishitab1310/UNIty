import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load the pre-trained Word2Vec model
embedding_file = '/Users/udaybindal/Downloads/glove.6B/glove.6B.300d.txt'

# Load word vectors into a dictionary
word_vectors = {}
with open(embedding_file, 'r', encoding='utf-8') as f:
    for line in f:
        values = line.split()
        word = values[0]
        vector = np.array(values[1:], dtype=np.float32)
        word_vectors[word] = vector

# Get the word vector for a specific word
word = 'early'
word_vector = word_vectors.get(word)

# Find the most similar words to a given word
similar_words = []
if word_vector is not None:
    for target_word, target_vector in word_vectors.items():
        similarity = cosine_similarity([word_vector], [target_vector])[0][0]
        similar_words.append((target_word, similarity))
similar_words = sorted(similar_words, key=lambda x: x[1], reverse=True)[:10]

# Print the word vector and similar words
print(f"Word Vector for '{word}': {word_vector}")
print(f"Similar Words to '{word}': {similar_words}")
