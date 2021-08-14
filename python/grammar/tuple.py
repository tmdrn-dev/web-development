#define
myTuple = 1, 2, 3
myTuple2 = (1,2,3)
print(type(myTuple), type(myTuple2))

myList = [1,2,3]
myTuple3 = tuple(myList)
print(type(myTuple3))

# update: not support
# append: not support
# remove: not support

# packing
a = 1
b = 'text'
c = a, b
print(c)

# unpacking
x, y = c
print(x, y)
print('unpacking:', *c)

x, y = y, x # swap
print(x,y)

# '*'
for a in enumerate(myTuple):
    print('{}번째 값:{}'.format(*a))

print(*myTuple)