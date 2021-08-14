area = []
for i in range(1,6):
    area = area + [i*i]
print(area)

area2 = [i*i for i in range(1,6)]
print(area2)

area3 = [i*i for i in range(1,11) if i < 6]
print(area3)

area4 = [(x,y) for x in range(1,6) for y in range(1,6)]
print(area4)

students = ['a', 'b', 'c']
scores = [10, 20, 30]

myDict = { student: score for student, score in zip(students, scores)}
print(myDict)
