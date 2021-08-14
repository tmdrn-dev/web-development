'''
8
70 30 70 40 60 50 90 80 
'''

from sys import stdin
read = stdin.readline

from collections import deque
N = int(input())
score = list(map(int, read().split()))

result = dict()
index = 1
for i in score:
    if i not in result:
        result[i] = deque()
    result[i].append(index)
    index += 1

score = sorted(score, reverse=True)

sol = list()
for i in score:
    sol.append(result[i].popleft())

print(sol[0], sol[1], sol[2])