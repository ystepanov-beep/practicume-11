PUNCTUATION = ".,!?;:'-—…()[]{}«»\""

sentence = "Программа получает на вход строку - предложение. " \
"Сформируйте список слов этого предложения. " \
"Знаки препинания присоединенные к словам должны быть удалены. " \
"Программа должна выводить список слов."
lst = sentence.split()
set_words = set()
clean_lst = []

for word in lst:
    clean_word = word.strip(PUNCTUATION)
    clean_lst.append(clean_word)
    for word in clean_lst:
        set_words.add(word)
clean_lst.clear()

for value in set_words:
    clean_lst.append(value)

print(clean_lst)