users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

print("Dave" in users)
print("Dave" in data)
print("Dave" in emptylist)
print(users[0])
print(users[-2])

print(users.index('Sara'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append('Elsa')
print(users)

users += ['Jason']
print(users)

users.extend(['JImmy', "Savage"])
print(users)

users.extend(data)
print(users)

users.insert(0, 'Bob')
print(users)

users
