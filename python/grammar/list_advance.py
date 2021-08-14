
#slice
list1 = [0,1,2,3,4,5]
list2 = list1[0:2]
print(list2) # 0,1
list3 = list1[:2]
print(list3) # 0,1
list4 = list1[2:] # 2,3,4,5
print(list4)
list5 = list1[:] # 0,1,2,3,4,5
print(list5)

#slice step
myList = list1[0:6:2]
print(myList)
myList[1:] = range(10,20) # 특정 범위 치환
print(myList)
myList[5:8] = [100] # 범위를 하나로 치환
print(myList)
del myList[5:8]
print(myList)