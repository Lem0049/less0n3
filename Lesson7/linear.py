arou = [1, 2, 3, 4, 510, 4532, 5, 6]


def search(elm, ar):
    for i in range(len(ar)):
        if ar[i] == elm:
            return i
    return -1


print(search(4, arou))
