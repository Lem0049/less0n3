ar = [x for x in range(1, 100, 3)]


def binar_search(el, ar):
    left = 0
    right = len(ar)
    mid = (left + right) // 2
    while mid != el and left <= right:
        left = 0
        right = len(ar)
        mid = (left + right) // 2
        if ar[mid] == el:
            return mid
        elif ar[mid] > el:
            right = mid
        else:
            left = mid
    else:
        return -1


print(binar_search(33, ar))
