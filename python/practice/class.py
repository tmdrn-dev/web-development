from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

N = int(input())
SF = list()

for _ in range(N):
    s,f = map(int, input().split())
    heappush(SF, (f,s))

print(SF)

current,count = 0,0

while SF:
    f,s = heappop(SF)
    if s >= current:
        count += 1
        current = f

print(count)