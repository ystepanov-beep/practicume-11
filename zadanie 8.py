def sort_string_characters(input_str: str) -> str:
    """""
    Sort all characters in a string alphabetically.
    Takes a string as input, converts it to a list of characters,
    sorts the list, converts it back to a string, and returns
    the resulting string.
    """""
    input_str = list(input_str)
    input_str.sort()
    output_str = "".join(input_str)

    return output_str      


input_str = "Напишите программу, которая использует следующую функцию. " \
"Функция принимает на вход строку в качестве аргумента, преобразует строку" \
" в список символов, сортирует список, преобразует список обратно в строку, " \
"и возвращает полученную строку."
print(sort_string_characters(input_str))