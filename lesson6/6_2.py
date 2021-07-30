import os , pickle


if not os.path.isfile('dairy.dat'):
    data = [0,1]
    data[0] = input("введите тему   :")
    data[1] = input('введите описание   Ж')
    file = open("dairy.dat", "wb")
    pickle.dump(data, file)
    file.close()
else:
    file = open("dairy.dat", "rb")
    data = pickle.load(file)
    file.close()

print('spisok del', data[0], ",", data[1])




