word = "प ए न्स इ ल"
# word = 'खाइनछ'
# word = ''
# word = 'अ क अ स'

word = 'ख उ क उ र ई'




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
    
with open('generated_nepali_text.txt', 'w', encoding='utf-8') as f :
    f.write(new_word)

# remove space from the word
# for words in dict_1:
    
#     new_word = word.replace(words, dict_1[words])


# print(new_word)
# print(new_word)

# print(new_word)


# #khukuri = "खुकुरी"
# word = "खुकुरी"



# # Iterate through each character in the word
# for char in word:
#     print(char, end=' ')
