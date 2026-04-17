lst1 = [int(x) for x in input("Введите первый список: ").split()]
lst2 = [int(x) for x in input("Введите второй список: ").split()]

start_pos = int(input("Начало диапазона: "))
end_pos = int(input("Конец диапазона: "))

start_idx = start_pos - 1
end_idx = end_pos

extracted = lst1[start_idx:end_idx][::-1]

del lst1[start_idx:end_idx]

lst2.extend(extracted)

print(lst2)
print(lst1)