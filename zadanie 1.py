lst = []
lst_1 = []

for _ in range(10):    
    lst.append(int(input()))

for i in range(8):
    lst_1.append(lst[i] + lst[i + 1])

print(lst_1)