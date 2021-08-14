'''
[입력 설명]
첫 줄에 미로의 크기 X, Y(1≤X, Y≤100)가 주어진다.
둘째 줄에 출발점 x, y 좌표와 도착점 x, y 좌표가 공백으로 구분하여 주어진다.
셋째 줄부터 미로의 정보가 길은 0, 벽은 1로 공백이 없이 들어온다.
주의 사항으로, 좌표는 좌측상단이 가장 작은 위치이며 이 위치의 좌표는 (1,1)이다.
8 7
1 2 7 5
11111111
00000111
10110011
10111001
10111101
10000001
11111111
[출력 설명]
첫 줄에 출발점에서 도착점까지 가장 빠른 시간을 출력한다.
9
'''
from sys import stdin
read = stdin.readline

maze_c, maze_r = map(int, read().split())
s_c, s_r, g_c, g_r = map(int, read().split())
start = (s_r-1, s_c-1)
goal = (g_r-1, g_c-1)
maze = [list(map(int, input())) for _ in range(maze_r)]

from collections import deque

def bfs():
    que = deque()
    que.append(start)
    maze[start[0]][start[1]] = -1

    while que:
        r, c = que.popleft()

        dr = [0, -1, 0, 1]
        dc = [1, 0, -1, 0]

        for i in range(4):
            row = r + dr[i]
            col = c + dc[i]

            if -1 < row < maze_r and -1 < col < maze_c:
                if maze[row][col] == 0:
                    maze[row][col] = maze[r][c]-1
                    que.append((row, col))

bfs()
print(-1*maze[goal[0]][goal[1]]-1)
