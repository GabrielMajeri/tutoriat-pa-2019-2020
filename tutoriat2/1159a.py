num_ops = int(input())
ops = input()

stones = 0

for op in ops:
    if op == '+':
        stones += 1
    else:
        stones -= 1

    if stones < 0:
        stones = 0

print(stones)
