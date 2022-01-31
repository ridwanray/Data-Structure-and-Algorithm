# Time complexity O(n)... Linear Time
# Linear search algorithm does not need
# list to be sorted because equal value is compare
# sequentially
def linear_search(numbers, target):
    """
    Returns the postion of target, else None
    """
    for i in range(0, len(numbers)):
        if numbers[i] == target:
            return i
    return None


def verify_index(index):
    if index is not None:
        print('Item found at index', index)
    else:
        print("Item not found")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = linear_search(numbers, 9)
verify_index(result)
