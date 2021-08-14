# https://codepro.lge.com/exam/18/%EA%B5%AD%EB%82%B4-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C/quiz/5
'''
곱셈 구현해야하는거 아닌가...????????????
10진수 연산 결과를 N진수로 변환해주기만 했는데 정답처리됨
'''
from sys import stdin
read = stdin.readline

n = int(input())
user_input = [list(map(str, read().split())) for _ in range(n)]

def ctoi(val):
    return int(val, 36)

def itoc(val):
    if 0 <= val and val < 10:
        return chr(val+48)
    elif 10 <= val and val < 36:
        return chr(val+55)
    else:
        raise ValueError

# def convertD(num, base):
#     sum = 0
#     negative = 1
#     if num[0] == '-':
#         negative = -1
#         num = num[1:]
#     size = len(num)
#     for i in range(size):
#         sum += ctoi(num[i]) * (base ** (size-1-i))
#     return sum * negative

def convertN(num, base):
    result = list()
    negative = ''
    if num < 0:
        negative = '-'
        num *= -1
    while num != 0:
        m, n = divmod(num, base)
        result.append(itoc(n))
        num = m
    result = reversed(result)
    return negative + ''.join(result)

for tc in user_input:
    base = int(tc[0])
    left = tc[1]
    right = tc[2]
    if left == '0' or right == '0':
        print('0')
    else:
        #print(convertN(convertD(left, base) * convertD(right, base), base))
        print(convertN(int(left, base) * int(right, base), base))