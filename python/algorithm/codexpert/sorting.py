'''
10
8 24 27 18 20 6 17 19 30 11 
'''

import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    A = list(map(int,readl().split()))
    return N, A

# 입력받는 부분
N, A = Input_Data()

# 여기서부터 작성
A = sorted(A)

# 출력하는 부분
print(*A)