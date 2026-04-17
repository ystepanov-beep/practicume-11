PUNCTUATION = ".,!?;:'-—…()[]{}«»\""

text = "Программа получает на вход текст, " \
"который вводится с клавиатуры. Признак окончания ввода " \
"текста - пустая строка. Программа должна вывести слова, " \
"в порядке от наиболее часто встречающегося к менее встречающемуся. " \
"Если слова встречаются в тексте одинаковое количество раз, то они должны " \
"выводиться в порядке их появления в тексте. " \
"Программа выводит каждое слово в " \
"отдельной строке в нижнем регистре. Знаки препинания должны быть исключены."
while True:
    line = input()
    if line == "":
        break
    text += line + " "
    break

raw_words = text.split()

word_count = {}
unique_words = []

for word in raw_words:
    clean_word = word.strip(PUNCTUATION).lower()
    if clean_word != '':
        if clean_word not in word_count:
            word_count[clean_word] = 0
            unique_words.append(clean_word)
        word_count[clean_word] += 1

unique_words.sort(key=word_count.get, reverse=True)

for word in unique_words:
    print(word)