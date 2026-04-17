lst = [int(x) for x in input().split()]

command = input()
direction = command[0]
shift = int(command[1:])

n = len(lst)
if n > 0:
    shift = shift % n

    if direction == 'R':
        lst = lst[-shift:] + lst[:-shift]
    elif direction == 'L':
        lst = lst[shift:] + lst[:shift]

print(lst)