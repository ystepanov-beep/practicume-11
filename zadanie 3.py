PUNCTUATION = ".,!?;:'-—…()[]{}«»\""

sentence = "Программа получает на вход строку - предложение. " \
"Сформируйте список слов этого предложения. " \
"Знаки препинания присоединенные к словам должны быть удалены. " \
"Программа должна выводить список слов."
lst = sentence.split()

clean_lst = []
for word in lst:
    clean_word = word.strip(PUNCTUATION)
    if clean_word != '': 
        clean_lst.append(clean_word)

print(clean_lst)