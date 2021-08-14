# https://codepro.lge.com/exam/18/%EA%B5%AD%EB%82%B4-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C/quiz/10
# 1번 공장 범위 구한 후 (DFS) 각 정점에서 BFS로 2번 공장에 닿기까지의 거리 중 최소 구하기
# 최적의 출발점 찾지 않고 시도해보기 -> tc 11번 실패 (runtime error)

from sys import stdin
read = stdin.readline

map_row, map_col = map(int, read().split())

map = [list(map(int, read().split())) for _ in range(map_row)]
factory_map = [[0]*map_col for _ in range(map_row)]

# get factory1 area
area = list()
def dfs(row, col, num):
    if num == 1:
        area.append((row, col))
    else:
        num = 100
    factory_map[row][col] = num

    r = [-1, 0, 1, 0]
    c = [0, 1, 0, -1]

    for i in range(4):
        dr = row + r[i]
        dc = col + c[i]

        if -1 < dr < map_row and -1 < dc < map_col:
            if map[dr][dc] == 1 and factory_map[dr][dc] == 0:
                dfs(dr, dc, num)

# numbering factory
num = 1
for i in range(map_row):
    for j in range(map_col):
        if map[i][j] == 1 and factory_map[i][j] == 0:
            dfs(i, j, num)
            num += 1

from collections import deque

# area1의 각 좌표에서 factory100에 닿을 때까지 탐색
bridge = float('inf')
def bfs():
    que = deque()
    for vertex in area:
        que.append(vertex)

        while que:
            row, col = que.popleft()

            r = [-1, 0, 1, 0]
            c = [0, 1, 0, -1]

            for i in range(4):
                dr = row + r[i]
                dc = col + c[i]

                if -1 < dr < map_row and -1 < dc < map_col:
                    if factory_map[dr][dc] == 100:
                        global bridge
                        bridge = min(factory_map[row][col], bridge)
                        continue

                    if factory_map[dr][dc] > factory_map[row][col] + 1 or factory_map[dr][dc] == 0:
                        factory_map[dr][dc] = factory_map[row][col] + 1
                        que.append((dr, dc))

bfs()
print(bridge-1)
