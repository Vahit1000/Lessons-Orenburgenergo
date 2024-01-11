people = [
    ['Tom', 24],
    ['Bob', 36],
    ['Sam', 25]
]

print(people)
print(people[0])
print(people[0][0])
print(people[0][1])

person = ['Bill', 18]
people.append(person)
print(people)

person = list()
person.append('Mike')
person.append(50)

people.append(person)
print(people)

print(people[-1][0])

for person in people:
    for item in person:
        print(item, end='\t')


