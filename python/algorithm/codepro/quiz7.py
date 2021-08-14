# https://codepro.lge.com/exam/18/%EA%B5%AD%EB%82%B4-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C/quiz/7

'''
1. bfs로 인접 좌표 뻗어 나가며 cost 합치기
2. 확산 단계를 적용하여 visited[dr][dc] = visited[row][col] 이전 단계는 선택하지 않도록 함.
3. 8개 항목 fail 발생
4. cost[dr][dc]가 0이면 cost[r][c] + matrix[dr][dc]로 update
5. cost[dr][dc]가 0이 아닌 경우 cost[r][c] + matrix[dr][dc]가 더 싸면 update
6. 0,0에 방문하지 않아야함
7. 모든 인접 vertext를 방문 후 factory 값 출력

!! 3번까지 진행 후 잘 안되어 최단 거리 문제 관련 검색한 결과
보통 heapq를 사용한 greedy 알고리즘, 최소 신장트리, 다익스트라 알고리즘 사용함.
'''

size = int(input())
matrix = [list(map(int, input())) for _ in range(size)]
cost = [[0]*size for _ in range(size)]

from collections import deque
def bfs():
    que = deque()
    que.append((0,0))

    r = [-1, 0, 1, 0]
    c = [0, 1, 0, -1]

    while que:
        row, col = que.popleft()
        for i in range(4):
            dr = row + r[i]
            dc = col + c[i]
            
            if not (dr == 0 and dc == 0):
                if (-1 < dr and dr < size) and (-1 < dc and dc < size):
                    if cost[dr][dc] == 0:
                        cost[dr][dc] = cost[row][col] + matrix[dr][dc]
                        que.append((dr, dc))
                    else:
                        if cost[dr][dc] > cost[row][col] + matrix[dr][dc]:
                            cost[dr][dc] = cost[row][col] + matrix[dr][dc]
                            que.append((dr, dc))

bfs()
print(cost[size-1][size-1])
