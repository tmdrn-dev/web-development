# https://codepro.lge.com/exam/18/%EA%B5%AD%EB%82%B4-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C/quiz/22

'''
7 1 4
pop&push 반복으로 구현 가능
M번째까지 pop push 이후 pop해서 visited에 저장
또 반복
'''
import sys
N, S, M = map(int, sys.stdin.readline().split())

from collections import deque
que = deque(i+1 for i in range(N))

def rotateque(que, S):
    while que[0] != S:
        que.rotate(1)

visited = list()

start = S + M - 1
rotateque(que, start)
current = que.popleft()
visited.append(current)

while que:
    index = int((0+M-1)%len(que))
    start = que[index]
    rotateque(que, start)
    current = que.popleft()
    visited.append(current)

res = ''
for i in visited:
    res += str(i)
    res += ' '
print(res)
