import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    A = list(map(int, readl().split()))
    return N, A


def Push(d):
    global stack, sp
    # 여기서부터 구현
    if sp > 0:
        stack.append(d)
        sp -= 1
        return sp
    else:
        return -1


def Pop():
    global stack, sp
    # 여기서부터 구현
    if sp < 4:
        sp += 1
        return stack.pop()
    else:
        return -1


def Solve():
    for i in range(N):
        if A[i] > 0:
            r = Push(A[i])
            if r == -1: print(-1, end=' ')
        else:
            r = Pop()
            if r == -1: print(-1, end=' ')
            else: print(r, end=' ')


stack = [0]*4
sp = 4

N, A = Input_Data()
Solve()