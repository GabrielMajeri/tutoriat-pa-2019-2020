"""
The equations for two lines are:
y = x + p
y = -x + q

For them to intersect their y must be equal:
    x + p = -x + q <=> 2x = q - p

It follows that q - p must be even, so q and p must have the same parity.
"""


def read_coefficients():
    num_lines = int(input())

    evens = 0
    odds = 0
    for c in input().split():
        c = int(c)

        if c % 2 == 0:
            evens += 1
        else:
            odds += 1

    return evens, odds


num_tests = int(input())

for test in range(num_tests):
    pos_even, pos_odd = read_coefficients()
    neg_even, neg_odd = read_coefficients()

    answer = pos_even * neg_even + pos_odd * neg_odd
    print(answer)