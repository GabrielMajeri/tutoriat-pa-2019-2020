message = input()

start = 0
ok = True

for char in 'hello':
    idx = message.find(char, start)
    if idx == -1:
        ok = False
        break

    start = idx + 1

print("YES" if ok else "NO")
