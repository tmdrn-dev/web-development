# define
myList = [1, 2, 3]
# myList = list(range(3))
print(myList)

# update element
myList[-1] = 33 # [-1]: last element
print(myList)

# append
myList.append(4)
print(myList)

# remove
del myList[0] # index
print(myList)
myList.remove(2) # value
print(myList)

# merge list
# myList2 = [5,6,7]
myList2 = list(range(5,8))
myList3 = myList + myList2
print(myList3)

# check value in list
print(4 in myList)

# for
for ele in myList3:
    print(ele, end=' ')

for ele in range(len(myList3)):
    print(ele)

state = ['a', 'b', 'c']
for i, ele in enumerate(state):
    print("""{}.'{}'""".format(i+1, ele))

myList.clear()