# https://www.acmicpc.net/problem/1697
N, M = map(int, input().split())
visited = [float('inf')] * 1000001

from collections import deque
def bfs():
    que = deque()
    que.append((N, 0))

    while que:
        n, cnt = que.popleft()

        dn = [n-1, n+1, n*2]
        for i in range(3):
            if 0 <= dn[i] <= 100000:
                if visited[dn[i]] > cnt+1:
                    visited[dn[i]] = cnt+1
                    que.append((dn[i], cnt+1))

if N == M:
    print(0)
else:
    bfs()
    print(visited[M])
