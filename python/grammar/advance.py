#몫과 나머지
#divmod
a, b = 5, 3
print(*divmod(a,b))

#진법 변환
#int
num, base = '12', 3
print(int(num,base))

#문자열 정렬
#ljust #center #rjust
s = 'abc'
n = 7
print(s.ljust(n))
print(s.center(n))
print(s.rjust(n))

import string as str
print(str.ascii_lowercase)

#행렬 뒤집기
#map #zip
myList = [[1,2,3], [4,5,6], [7,8,9]]
print(*myList) # [1, 2, 3] [4, 5, 6] [7, 8, 9]
print(*zip(*myList)) # (1, 4, 7) (2, 5, 8) (3, 6, 9)
print(list(map(list, zip(*myList))))

#문자열 나누기
#split
time_str = "21:09:10"
time_list = time_str.split(':')
print(time_list)

#문자열 합치기
#join
time_list = ':'.join(time_list)
print(time_list)

#리스트 반복
print('*'*3) # ***
print([1,2]*3) # [1,2,1,2,1,2]

#가장 큰 수 inf
max_val = float('inf')
min_val = float('-inf')
