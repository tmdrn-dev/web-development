'''
[입력 설명]
첫 줄은 장기판 행의 수(N)와 열의 수(M)를 받는다.(1≤N,M≤100)
둘째 줄은 말이 있는 위치의 행(R), 열(C)의 수와 졸이 있는 위치의 행(S), 열(K)의 수를 입력 받는다. 
단, 장기판의 제일 왼쪽 위의 위치가 (1,1)이다.
각 행과 열은 R(1≤R≤N), C(1≤C≤M), S(1≤S≤N), K(1≤K≤M)이다.
9 9
3 5 2 8
[출력 설명]
말이 졸을 잡기 위한 최소 이동 횟수를 출력한다.
2
'''

from sys import stdin
read = stdin.readline

n, m = map(int, read().split())
r, c, s, k = map(int, read().split())
matrix = [[0]*m for _ in range(n)]

from collections import deque
def bfs():
    global r, c
    que = deque()
    que.append((r,c))

    while que:
        row, col = que.popleft()

        r = [-2, -1, 1, 2, 2, 1, -1, -2]
        c = [1, 2, 2, 1, -1, -2, -2, -1]

        for i in range(8):
            dr = row + r[i]
            dc = col + c[i]

            if -1 < dr < n and -1 < dc < m:
                if matrix[dr][dc] == 0:
                    matrix[dr][dc] = matrix[row][col] + 1
                    que.append((dr, dc))

bfs()
print(matrix[s][k])
