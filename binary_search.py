def binary_search(arrays, target):
    low = 0
    up = len(arrays) - 1
    mid = 0

    while low <= up:
        mid = low + (up - low) // 2
        # if the mid value is the target
        if arrays[mid] == target:
            return mid
        # if mid is less than target, ignore left
        elif arrays[mid] < target:
            low = mid + 1
        # if mid is higher than target,ignore right
        else:
            up = mid - 1
    return None


def verify(index):
    if index is not None:
        print('The search item is found at index', index)
    else:
        print('Search item not found')


items = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = binary_search(items, 5)
verify(result)
