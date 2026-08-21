def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6]]
    print(transpose(m))  # [[1, 4], [2, 5], [3, 6]]
