# define
myDict = {'one':1, 'two':2}
print(myDict)

# update element
myDict['one'] = 11
print(myDict)

# append
myDict['three'] = 3
myDict['four'] = 4
print(myDict)

# remove
myDict.pop('two')
del(myDict['one'])
print(myDict)

# merge dictionary
myDict2 = {'five':5, 'six':6}
myDict.update(myDict2)
print(myDict)

# check element in dictionary
print('three' in myDict.keys()) # 'three' in myDict.keys()
print(3 in myDict.values())

# for
for key in myDict.keys(): # == for key in myDict:
    print(key)

for value in myDict.values():
    print(value)

for key, value in myDict.items():
    print('{}={}'.format(key, value))

# '*'
print(*myDict)

myDict.clear()