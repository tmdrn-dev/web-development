# https://codepro.lge.com/exam/18/%EA%B5%AD%EB%82%B4-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C/quiz/9
'''
8
7 2 1 8 4 3 5 6 
'''

from sys import stdin
read = stdin.readline

num = int(input())
array = list(map(int, read().split()))

from itertools import combinations

comb = dict()
for i in range(1, num+1):
    if i%2 == 1:
        comb[i] = list()
        comb[i] = list(combinations(range(num), i))

def getMushroom(data):
    sum = 0
    negative = 1
    for i in data:
        sum += array[i] * negative
        negative *= -1
    return sum

height = 0
for select in comb:
    for i in comb[select]:
        if getMushroom(i) > height:
            height = getMushroom(i)

print(height)


# 범위 관련된 runtime error 발생
# data 범위 제대로 설정할 필요 있음
# 접근 자체가 잘못됨 다시 풀자
