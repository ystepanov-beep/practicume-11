lst = list(map(int, input().split()))
meaning = 0
count = 0

for i in range(len(lst)):
    meaning += lst[i]
    count += 1

print(meaning / count)