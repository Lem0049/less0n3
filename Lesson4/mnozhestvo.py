mnozhestvo1 = {'red','green','blue','yellow'}
mnozhestvo2 = {'green', 'blue', 'brown'}
mnozhestvo1.add('orange')
print(mnozhestvo1)
mnozhestvo2.remove('blue')
print(mnozhestvo2)

a = 5

mnozhestvo3 = mnozhestvo1.copy()
mnozhestvo3.add('cyan')
print(mnozhestvo3)

print(mnozhestvo1 | mnozhestvo3) #объединение множеств
print(mnozhestvo1 & mnozhestvo3) # пересечение
print(mnozhestvo1 - mnozhestvo2) # разность множеств
