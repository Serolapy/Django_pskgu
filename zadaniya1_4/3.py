text = input("Введите текст: ")	# слово1 слово2 слово1 большоеслово
words = text.split(" ") #массив из слов
long_word = ""			#самое длинное слово
list_word = {}			#слово - количество повторений

for word in words:
	
	list_word[word] = list_word.get(word, 0) + 1
	if len(word) > len (long_word):
		long_word = word
	
chastoe_slovo = {"num": 0, "word": ''}
for word in list_word.keys():
	if list_word[word] > chastoe_slovo["num"]:
		chastoe_slovo["num"] = list_word[word]
		chastoe_slovo["word"] = word

print("Частовстречающееся слово: ", chastoe_slovo["word"])
print("Самое длинное слово: ", long_word)