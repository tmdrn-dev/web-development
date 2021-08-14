#https://www.acmicpc.net/problem/2805

from sys import stdin
read = stdin.readline

N, M = map(int, read().split())
tree = list(map(int, read().split()))
tree = sorted(tree)

# print(N, M, tree)

import bisect

def find(a, i):
    idx = bisect.bisect_left(a, a[i])
    if idx!=len(a) and a[idx] == a[i]:
        return idx
    return -1

start = 0
end = len(tree)
mid = int(int(start+end)/2)

print(mid, find(tree, mid))