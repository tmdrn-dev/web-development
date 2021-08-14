'''
11
1 2 3 4 0 0 0 5 0 0 0
'''

import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    A = list(map(int, readl().split()))
    return N, A


def Push(d):
    global queue, wp, rp
    # 여기서부터 작성
    if wp == len(queue):
        return 0
    queue[wp] = d
    wp = wp+1
    return 1

def Pop():
    global queue, wp, rp
    # 여기서부터 작성
    if wp == rp:
        return 0
    res = queue[rp]
    rp = rp+1
    return res

def Solve():
    for i in range(N):
        if A[i] > 0:
            r = Push(A[i])
            if r == 0: print(-1, end=' ')
        else:
            r = Pop()
            if r == 0: print(-1, end=' ')
            else: print(r, end=' ')


queue = [0]*5
wp = 0
rp = 0

# 입력받는 부분
N, A = Input_Data()

# 여기서부터 작성
Solve()
