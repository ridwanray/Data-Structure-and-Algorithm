def linear_search(items, target):

    for i in range(0, len(items)):
        if items[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print('item found at index', index)
    else:
        print('Item not found')


numbers = [1, 2, 3, 4, 5, 6]
result = linear_search(numbers, 43)
verify(result)
