a = map(int, ['10', '20','30'])
print(*a)

data = ['Ivan', 'Petr', 'Boris']

print(*map(len, data))


a = [x for x in range(10)]
a = map(lambda x: x * 5, a)
print(*a)