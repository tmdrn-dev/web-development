'''
[입력 설명]
첫째 줄에 N 이 입력된다. (1≤N≤200,000)
둘째 줄에 배열에 저장 되어있는 N개의 숫자가 순서대로 공백으로 구분되어 입력된다.
셋째 줄에 M 이 입력된다. (1≤M≤200,000)
넷째 줄에 M개의 탐색할 숫자가 순서대로 공백으로 구분되어 입력된다.
(이 숫자는 정렬 되어있지 않다)
10
1 1 1 6 9 11 13 17 19 20 
2
1 9 
[출력 설명]
입력 넷째 줄에서 주어진 탐색할 숫자의 배열 내 저장된 개수를 차례대로 출력한다.
3 1 
'''

import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    data = [0] + list(map(int,readl().split()))
    T = int(readl())
    num = list(map(int,readl().split()))
    return N, data, T, num

# 입력받는 부분
N, data, T, num = Input_Data()

# 여기서부터 작성
import bisect

sol = ''
for i in num:
    left = bisect.bisect_left(data, i)
    right = bisect.bisect_right(data, i)
    sol += str(right-left)
    sol += ' '

print(sol)