n, k = input().split()
n, k = int(n), int(k)

for _ in range(k):
    if n % 10 == 0:
        n //= 10
    else:
        n -= 1

print(n)
