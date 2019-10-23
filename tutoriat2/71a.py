def solve(word):
    if len(word) <= 10:
        return word

    n = len(word) - 2

    return word[0] + str(n) + word[-1]


num_tests = int(input())

for _ in range(num_tests):
    print(solve(input()))
