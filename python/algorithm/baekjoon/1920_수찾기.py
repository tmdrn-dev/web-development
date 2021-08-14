# https://www.acmicpc.net/problem/1920

from sys import stdin
read = stdin.readline

N = int(input())
A = list(map(int, read().split()))
A = sorted(A)

M = int(input())
B = list(map(int, read().split()))

def search(A, N):
    import bisect
    i = bisect.bisect_left(A, N)
    if i != len(A):
        if A[i] == N:
            return 1
    return 0

for i in B:
    print(search(A, i))
