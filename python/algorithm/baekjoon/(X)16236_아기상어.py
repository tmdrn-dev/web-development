# https://www.acmicpc.net/problem/16236

from sys import stdin
read = stdin.readline

matSize = int(input())
matrix = [list(map(int, read().split())) for _ in range(matSize)]

from collections import deque
def bfs(visited, start, sharkSize):
    target = dict()
    queue = deque()
    queue.append(start)

    r = [1, 0, -1, 0]
    c = [0, -1, 0, 1]

    while queue:
        nextCord = queue.popleft()
        row, col = nextCord

        for i in range(len(r)):
            dr = row + r[i]
            dc = col + c[i]
            if -1 < dr < matSize and -1 < dc < matSize:
                if matrix[dr][dc] <= sharkSize and visited[dr][dc] == 0:
                    visited[dr][dc] = visited[row][col] + 1
                    queue.append((dr, dc))
                    if 0 < matrix[dr][dc] < sharkSize:
                        if visited[dr][dc] not in target.keys():
                            target[visited[dr][dc]] = set()
                        target[visited[dr][dc]].add((dr, dc))

    matrix[start[0]][start[1]] = 0
    return target

distance = 0
sharkSize = 2
sharkExp = 0
starting = set()
for x, row in enumerate(matrix):
    for y, col in enumerate(row):
        if col == 9:
            starting = (x, y)

while starting:
    visited = [[0] * matSize for _ in range(matSize)]
    target = bfs(visited, starting, sharkSize)
    if target:
        row, col = starting = sorted(target[min(target)])[0]
        distance += visited[row][col]
        matrix[row][col] = 9
        sharkExp += 1
        if sharkExp == sharkSize:
            sharkSize += 1
            sharkExp = 0
    else:
        starting = None

print(distance)