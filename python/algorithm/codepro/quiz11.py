# https://codepro.lge.com/exam/18/%EA%B5%AD%EB%82%B4-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C/quiz/11
'''
5 7
1 2 5
3 2 14
2 4 5
1 3 10
4 3 15
5 4 15
3 5 8
'''

from sys import stdin
read = stdin.readline

node_num, edge_num = map(int, read().split())
distance = [[float('inf')]*(node_num) for _ in range(node_num)]
graph = dict()
for _ in range(edge_num):
    i, j, val = map(int, read().split())
    if i not in graph:
        graph[i] = list()
    if j not in graph:
        graph[j] = list()

    graph[i].append((val, j))
    graph[j].append((val, i))
    graph[i] = sorted(graph[i])
    graph[j] = sorted(graph[j])

from collections import deque
def bfs(start):
    que = deque()
    que.append(start)
    distance[start-1][start-1] = 0

    while que:
        que = deque(sorted(que))
        current = que.popleft()
        for val, next in graph[current]:
            if distance[start-1][next-1] > distance[start-1][current-1] + val:
                distance[start-1][next-1] = distance[start-1][current-1] + val
                que.append(next)

for i in graph:
    bfs(i)

farthest = list()
for i in distance:
    farthest.append(max(i))

print(min(farthest))