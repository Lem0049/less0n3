arou = [1, 2, 3, 4, 510, 4532, 4, 6]


def search(elm, ar):
    for i in range(len(ar)):
        c= []
        if ar[i] == elm:
            c.append(i)
            return c
    return -1


print(search(4, arou))
