'''
[입력 설명]
첫 번째 줄에는 연 잎의 수 N(3 ≤ N ≤ 1,000)이 주어진다.
두 번째 줄부터 N개의 줄에는 각 연 잎의 좌표가 주어진다. 모든 좌표는 0 이상 108 이하이다.
5
3
1
10
7
4
[출력 설명]
개구리가 오른쪽으로 도약하는 경우의 수를 출력한다.
4
'''

import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    pos = [int(readl()) for _ in range(N)]
    return N, pos

sol = -1
# 입력받는 부분
N, pos = Input_Data()
# 여기서부터 작성
import bisect
pos = sorted(pos)

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return i
    raise ValueError

def find_le(a, x):
    'Find rightmost item less than or equal to x'
    i = bisect.bisect_right(a, x)
    if i:
        return i-1
    raise ValueError

for start in range(N-1):
    for mid in range(start+1, N):
        distance = pos[mid]-pos[start]
        try:
            lower_end = find_ge(pos, pos[mid]+distance)
        except:
            continue
        try:
            upper_end = find_le(pos, pos[mid]+distance*2)
            if lower_end == upper_end:
                sol+=1
            elif upper_end > lower_end:
                sol += upper_end-lower_end+1
        except:
            sol += 1

print(sol+1)