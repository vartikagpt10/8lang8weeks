states = {
    'oregon' : 'or',
    'florida' : 'fl',
    'california' : 'ca',
    'new york' : 'ny'
}

cities = {
    'ca' : 'san francisco',
    'mi' : 'detroit',
    'fl' : 'jacksonville'
}

cities['ny'] = 'new york'

for i in cities:
    print(cities[i])
print('*'*20)

stuff = {}
stuff[1] = 'yeet'

print(stuff[1])
print('*' * 5)

for abbrev,state in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}")

cities['tx'] = 'texas'
print(cities['tx'])