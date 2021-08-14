'''
[입력 설명]
첫 줄에는 상자의 크기를 나타내는 두 정수 M, N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 
단, 2≤M, N≤1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 
즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 
하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
[출력 설명]
여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 
만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
8
'''

from sys import stdin
read = stdin.readline

M, N = map(int, read().split())
matrix = [list(map(int, read().split())) for _ in range(N)]

tomato = list()
for r in range(N):
    for c in range(M):
        if matrix[r][c] == 1:
            tomato.append((r,c))

from collections import deque
def bfs():
    que = deque()
    for i in tomato:
        que.append(i)

    while que:
        r, c = que.popleft()

        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        for i in range(4):
            row = r + dr[i]
            col = c + dc[i]

            if -1 < row < N and -1 < col < M:
                if matrix[row][col] == 0 and matrix[row][col] != -1:
                    matrix[row][col] = matrix[r][c]+1
                    que.append((row, col))

if len(matrix)*len(matrix[0]) == len(tomato):
    print(0)
else:
    bfs()

day = 0
for row in matrix:
    if 0 in row:
        print(-1)
    else:
        day = max(day, max(row))
print(day-1)