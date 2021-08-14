# https://codepro.lge.com/exam/18/%EA%B5%AD%EB%82%B4-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C/quiz/8
'''
4
2 10
2 8
3 4
4 12
'''

from itertools import combinations
from sys import stdin
read = stdin.readline

n = int(input())
filters = {i+1: tuple(map(int, read().split())) for i in range(n)}

combi = dict()
for i in range(1, n+1):
    combi[i] = list(combinations(filters, i))

count = 0
result = float('inf')
for i in combi:
    for selected in combi[i]:
        refl = 1; proj = 0
        for num in range(len(selected)):
            refl *= filters[selected[num]][0]
            proj += filters[selected[num]][1]
        if abs(refl-proj) < result:
            result = abs(refl-proj)
            count = i

print(n-count)
