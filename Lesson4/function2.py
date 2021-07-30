def multiple_input(n):
    result = []
    for i in range(n):
        result.append(int(input('введите число: ')))
    return result


triple_input = multiple_input(3)
quatro_input = multiple_input(4)

print(triple_input)
print(quatro_input)


def end_of_programm():
    import datetime
    print('game over')
    print('it was great', datetime.datetime.now())

end_of_programm()

