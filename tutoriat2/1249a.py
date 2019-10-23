def solve(students):
    # Order the students by increasing skill level
    students.sort()

    for i in range(len(students) - 1):
        # If two consecutive students have the same skill level,
        # we'll need an extra team
        if abs(students[i] - students[i + 1]) == 1:
            return 2

    return 1


num_tests = int(input())

for _ in range(num_tests):
    num_students = int(input())
    answer = solve([int(x) for x in input().split()])
    print(answer)
