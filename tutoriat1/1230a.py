def check_possible(nums):
    """Checks if its possible to split 4 bags of candies
    equally between Dawid's two friends."""

    nums.sort()

    smallest = nums[0]
    biggest = nums[3]

    # The only possibility is for the biggest to be the sum of the others
    # or for the biggest and the smalles to be equal to the sum of the remaining two
    return (biggest == (nums[0] + nums[1] + nums[2])
            or (biggest + smallest) == (nums[1] + nums[2]))


a, b, c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)

if check_possible([a, b, c, d]):
    print('YES')
else:
    print('NO')
