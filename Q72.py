def chunk_list(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]


if __name__ == "__main__":
    print(chunk_list([1, 2, 3, 4, 5, 6, 7], 3))  # [[1,2,3],[4,5,6],[7]]
