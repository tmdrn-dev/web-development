# https://www.acmicpc.net/problem/2667

size = int(input())
matrix = [list(map(int, input())) for _ in range(size)]
visited = [[0]*size for _ in range(size)]

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 0:
            visited[row][col] = 1

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

apt = list()
count = 0

def dfs(row, col):
    visited[row][col] = 1

    global count
    if matrix[row][col] == 1:
        count += 1

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if (nr > -1 and nr < size) and (nc > -1 and nc < size):
            if visited[nr][nc] == 0 and matrix[nr][nc] == 1:
                dfs(nr, nc)

for row in range(size):
    for col in range(size):
        if visited[row][col] == 0 and matrix[row][col] == 1:
            dfs(row, col)
            apt.append(count)
            count = 0

print(len(apt))
for i in sorted(apt):
    print(i)