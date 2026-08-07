def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    print(flatten([1, [2, 3, [4, 5]], 6, [[7], 8]]))  # [1,2,3,4,5,6,7,8]
