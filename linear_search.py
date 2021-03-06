def linear_search(numbers, target):
    """
    Returns the index position if found, else retun None
    """
    for i in range(0, len(numbers)):
        if numbers[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print('Item found at index', index)
    else:
        print('Search item not found')


items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

result = linear_search(items, 2)
verify(result)
