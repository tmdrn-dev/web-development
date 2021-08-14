# https://www.acmicpc.net/problem/7576

from collections import deque
from sys import stdin
read = stdin.readline

m, n = map(int, read().split())
matrix = [list(map(int, read().split())) for _ in range(n)]

startVertex = deque()
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == 1:
            startVertex.append((row, col))

def bfs(vertext):
    r = [-1, 0, 1, 0]
    c = [0, 1, 0, -1]

    while vertext:
        row, col = vertext.popleft()
        for i in range(4):
            dr = row + r[i]
            dc = col + c[i]

            if (-1 < dr and dr < n) and (-1 < dc and dc < m):
                if matrix[dr][dc] == 0:
                    matrix[dr][dc] = matrix[row][col] + 1
                    vertext.append((dr, dc))

bfs(startVertex)

result = 0
for row in matrix:
    if 0 in row:
        result = 0
        break
    for col in row:
        result = max(result, col)

print(result-1)