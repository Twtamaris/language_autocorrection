from collections import namedtuple
from gensim.models import Word2Vec

# Define data structure for word and its embedding
WordEmbedding = namedtuple("WordEmbedding", ["word", "embedding"])

def load_word_embeddings(filename):

  embeddings = {}
  with open(filename, "r") as f:
    for line in f:
      word, *embedding = line.strip().split()
      embedding = list(map(float, embedding))
      embeddings[word] = WordEmbedding(word, embedding)
  return embeddings

def get_nearest_neighbors(model, word, k):

  embedding = model[word].embedding
  distances = {}
  for other_word, other_embedding in model.items():
    distances[other_word] = distance(embedding, other_embedding)
  return sorted([(word, distance) for word, distance in distances.items()], key=lambda x: x[1])[:k]

def distance(embedding1, embedding2):

  # You can use different distance measures here, such as Euclidean distance
  return sum((a - b) ** 2 for a, b in zip(embedding1, embedding2))

# Load the pre-trained word embeddings
model = load_word_embeddings("word_embeddings.txt")

# Prompt the user for input
user_input = input("Enter a word: ")

# Find and display the nearest neighbors
k = 5  # Number of nearest neighbors to display
nearest_neighbors = get_nearest_neighbors(model, user_input, k)
print(f"Nearest neighbors of '{user_input}':")
for word, distance in nearest_neighbors:
  print(f"- {word}: {distance:.2f}")
