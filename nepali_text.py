import pickle


# word = "प ए न्स इ ल"
# word = 'खाइनछ'
# word = ''
# word = 'अ क अ श'

word = input("Enter a word: ")

# word = 'ख उ क उ र ई'

# for letters in word:
#     print(letters, end=' ')

dict_1 = {
    "आ" : "ा",
    "उ" : "ु",
    "ई" : "ी",
    "इ" : "ि",
    "ऊ" : "ू",
    "ऋ" : "ृ",
    "ए" : "े",
    "ऐ" : "ै",
    "ओ" : "ो",
    "औ" : "ौ",
    "अं" : "ँ",
    "अः" : "ः",
    "अ" : "ा"
}

word = word.replace(" ", "")

new_word = ""
for i, letter in enumerate(word):
    if i == 0 and letter in dict_1:
        new_word += letter
    elif letter =="इ" and word[i+1] == "न":
        new_word += "इ"
    
    elif letter in dict_1:
        new_word += dict_1[letter]
    else:
        new_word += letter

print(new_word)

with open('knn_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('nepali_dataset.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    words = data.split()

letters = sorted(set(''.join(words)))
letter_to_index = {letter: idx for idx, letter in enumerate(letters)}


input_letter_representation = [0] * len(letters)
for letter in new_word:
    if letter in letter_to_index:
        input_letter_representation[letter_to_index[letter]] += 1

# Find nearest neighbors based on letter-level representations
distances, indices = model.kneighbors([input_letter_representation])

# Print nearest words
nearest_words = [words[idx] for idx in indices.flatten()]
with open("generated_nepali_text.txt", "w", encoding='utf-8') as f:
    f.write(f'{new_word} : {nearest_words}')

