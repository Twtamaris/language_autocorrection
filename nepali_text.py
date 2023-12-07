word = " च इ य अ"




for letters in word:
    print(letters, end=' ')

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
# remove space from the word
word = word.replace(" ", "")
for words in dict_1:
    
    new_word = word.replace(words, dict_1[words])


# print(new_word)
# print(new_word)
with open('nepali_text.txt', 'w', encoding='utf-8') as f :
    f.write(new_word)

print(new_word)


# #khukuri = "खुकुरी"
# word = "खुकुरी"



# # Iterate through each character in the word
# for char in word:
#     print(char, end=' ')
