number = int(input())
lst = []

for i in range(1, number + 1):
    if number % i == 0:
        lst.append(i)

print(lst)