import pickle

fileName = 'user.dat'

name = 'Tom'
age = 35

with open(fileName, 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    file.close()

with open(fileName, 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print(f'{name} - {age}')
    file.close()
