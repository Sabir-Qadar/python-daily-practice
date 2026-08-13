def bubble_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    print(bubble_sort([5, 2, 9, 1, 5, 6]))  # [1,2,5,5,6,9]
