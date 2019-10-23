def read_matrix():
    """Reads the matrix and returns the row and column of the 1"""
    for i in range(5):
        row = [int(x) for x in input().split()]
        for j in range(5):
            if row[j] == 1:
                return i, j


i, j = read_matrix()
distance = abs(i - 2) + abs(j - 2)
print(distance)