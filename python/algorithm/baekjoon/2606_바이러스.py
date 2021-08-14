# https://www.acmicpc.net/problem/2606

from sys import stdin
read = stdin.readline

networks = dict()
for i in range(int(read())):
    networks[i+1] = set()

for i in range(int(read())):
    a,b = map(int, read().split())
    networks[a].add(b)
    networks[b].add(a)

visited = list()
def dfs(node):
    visited.append(node)

    for nextNode in networks[node]:
        if nextNode not in visited:
            dfs(nextNode)

dfs(1)
print(len(visited)-1)
