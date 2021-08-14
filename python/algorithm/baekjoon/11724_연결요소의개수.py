# https://www.acmicpc.net/problem/11724

import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline

graph = dict()
n, m = map(int, read().split())

for i in range(n):
    graph[i+1] = set()

for i in range(m):
    u, v = map(int, read().split())
    graph[u].add(v)
    graph[v].add(u)

for i in graph:
    print(graph[i])

visited = list() # list 순회가 배열 access보다 느리다.
def dfs(node):
    visited.append(node)

    for nextNode in graph[node]:
        if nextNode not in visited:
            dfs(nextNode)

count = 0
for i in range(n):
    if i+1 not in visited:
        dfs(i+1)
        count += 1

print(count)
