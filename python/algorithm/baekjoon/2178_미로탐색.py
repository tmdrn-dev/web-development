# https://www.acmicpc.net/problem/2178

from sys import stdin
read = stdin.readline

from collections import deque

n, m = map(int, read().split())
matrix = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

# 행렬 최단경로 bfs 사용!!
def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1

    r = [0, 1, 0, -1]
    c = [1, 0, -1, 0]

    while queue:
        row, col = queue.popleft()
        for i in range(4):
            dr = row + r[i]
            dc = col + c[i]

            if -1 < dr < n and -1 < dc < m:
                if visited[dr][dc] == 0 and matrix[dr][dc] == 1:
                    visited[dr][dc] = visited[row][col] + 1
                    queue.append((dr, dc))

bfs()

# print(visited)
print(visited[n-1][m-1])
