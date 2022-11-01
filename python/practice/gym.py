'''
5 3
1 2 3 4 5
1 3
2 4
2 5
'''

import heapq
import sys
read = sys.stdin.readline

N, M = map(int, read().split())
W = list(map(int, read().split()))
AB = dict()

for i in range(N):
    AB[i+1] = list()

for _ in range(M):
    A, B = map(int, read().split())
    heapq.heappush(AB[A], -W[B-1])
    heapq.heappush(AB[B], -W[A-1])

# print(W)
# print(AB)

count = 0
for i in range(1, N+1):
    if len(AB[i]) > 0 and (W[i-1] > -AB[i][0]):
        #print("W[{}]: {}, AB[{}]: {}".format(i-1, W[i-1], i, -AB[i][0]))
        count += 1
    elif len(AB[i]) == 0:
        count += 1

print(count)