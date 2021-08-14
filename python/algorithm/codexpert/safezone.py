'''
입력 설명
첫째 줄에는 어떤 지역을 나타내는 2차원 배열의 행과 열의 개수를 나타내는 수 N이 입력된다. 
N은 2 이상 100 이하의 정수이다. 둘째 줄부터 N 개의 각 줄에는 2차원 배열의 첫 번째 행부터 N번째 행까지 순서대로 한 행씩 높이 정보가 입력된다. 
각 줄에는 각 행의 첫 번째 열부터 N번째 열까지 N 개의 높이 정보를 나타내는 자연수가 빈 칸을 사이에 두고 입력된다. 높이는 1이상 100 이하의 정수이다. 
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
출력 설명
첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다.
5
'''

from sys import stdin
read = stdin.readline

N = int(input())
matrix = [list(map(int, read().split())) for _ in range(N)]

from collections import deque
def bfs(visited, i, j, height, cnt):
    que = deque()
    que.append((i, j))
    visited[i][j] = cnt+1

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    while que:
        r, c = que.popleft()
        for k in range(4):
            row = r + dr[k]
            col = c + dc[k]

            if -1 < row < N and -1 < col < N:
                if visited[row][col] == 0 and matrix[row][col] > height:
                    visited[row][col] = cnt+1
                    que.append((row, col))

def getArea(height):
    cnt = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and matrix[i][j] > height:
                bfs(visited, i, j, height, cnt)
                cnt += 1
    return cnt

sol = 0
for i in range(1, 101):
    area = getArea(i)
    if sol < area:
        sol = area

print(sol)
