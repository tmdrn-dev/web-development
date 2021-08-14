# https://www.acmicpc.net/problem/1260

from sys import stdin
read = stdin.readline

n, m, v = map(int, read().split())

graph = dict()
for node in range(n):
    graph[node+1] = list() # note: set()로 만들어서 작은 순서로 접근해야하는 부분 대응하지 못함

for edge in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    graph[node] = sorted(graph[node])

visited = list()
def dfs(node):
    visited.append(node)

    for nextNode in graph[node]:
        if nextNode not in visited:
            dfs(nextNode)

dfs(v)
print(*visited)

from collections import deque
visited.clear()

def bfs(node):
    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)

        for nextNode in graph[node]:
            if nextNode not in visited:
                queue.append(nextNode)

bfs(v)
print(*visited)
