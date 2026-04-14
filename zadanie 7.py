lst = list(map(int, input().split()))
not_even = 0
even = 0

for number in lst:
    if number % 2 == 1:
        not_even += number
    else:
        even += number

print(f"Сумма четных чисел:{even}")
print(f"Сумма нечетных чисел:{not_even}")