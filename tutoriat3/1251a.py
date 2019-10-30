num_tests = int(input())

for _ in range(num_tests):
    s = input()

    not_broken = set()
    i = 0
    while i < len(s):
        if i == len(s) - 1 or s[i] != s[i + 1]:
            not_broken.add(s[i])
        else:
            i += 1

        i += 1

    not_broken = sorted(not_broken)

    print(''.join(not_broken))
