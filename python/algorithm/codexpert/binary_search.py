'''
[입력 설명]
첫 번째 줄에 N(1≤N≤50,000)이 주어진다. N은 정렬되어 주어지는 데이터의 수이다.
두 번째 줄에는 N개의 서로 다른 수가 정렬되어 주어진다. 각 수는 공백 하나로 분리되어 주어진다.
세 번째 줄에는 데이터에서 찾아야 할 특정한 수의 개수 T(1≤T≤10,000)가 주어진다. 즉, T가 3이면 3개의 수를 정렬된 데이터에서 찾아야 한다.
네 번째 줄에는 T개의 수가 공백 하나로 분리되어 주어진다.
7
2 4 9 10 14 23 32
3
6 23 9
[출력 설명]
찾아야 할 수가 정렬되어 주어진 데이터의 수 중에서 앞에서부터 몇 번째에 있는지 그 위치를 출력한다. 첫 번째 위치는 1이다. 만약, 찾으려는 수가 주어지는 데이터에 존재하지 않는다면, 0을 출력한다.
0
6
3
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

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    print(i, len(a), a[i], x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

for i in num:
    try:
        print(index(data, i))
    except:
        print(0)