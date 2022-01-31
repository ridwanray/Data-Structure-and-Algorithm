def recursive_binary_search(lists, target):
    if len(lists) == 0:
        return False
    else:
        mid = len(lists) // 2

        if lists[mid] == target:
            return True
        else:
            if lists[mid] < target:
                return recursive_binary_search(lists[mid+1:], target)
            else:
                return recursive_binary_search(lists[:mid-1], target)


def verify(status):
    print("Item Found:", status)


numbers = [1, 2, 3, 4, 5, 6]
result = recursive_binary_search(numbers, 9)
verify(result)
