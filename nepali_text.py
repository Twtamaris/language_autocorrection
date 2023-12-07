word = " च इ य अ"


new_word = word.replace("आ", "ा")
# new_word = word.replace("उ", "ु")
new_word = word.replace("ई", "ी")  
# for इ
new_word = word.replace("इ", "ि")
new_word = word.replace("ऊ", "ू")
# new_word = word.replace("ई", "ी")
new_word = word.replace("ऊ", "ू")
new_word = word.replace("ऋ", "ृ")
new_word = word.replace("ए", "े")
new_word = word.replace("ऐ", "ै")
new_word = word.replace("ओ", "ो")
new_word = word.replace("औ", "ौ")
new_word = word.replace("अं", "ँ")
new_word = word.replace("अः", "ः")
new_word = word.replace("अ", "ा")


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
