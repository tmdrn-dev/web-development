'''
[입력 설명]
첫 번째 줄에는 학교의 수를 나타내는 정수 N(1≤N≤100)이 주어진다. 다음 N개의 줄에 각 학교의 학생 수와 배정된 사과 개수를 나타내는 두 개의 정수가 주어진다. 학생 수와 사과 개수는 모두 1이상 100이하이다.
5
24 52
13 22
5 53
23 10
7 70
[출력 설명]
남은 사과의 총 개수를 나타내는 정수를 출력한다.
26
'''

import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    list_data = [list(map(int,readl().split()))for _ in range(N)]
    S = [list_data[n][0] for n in range(N)]
    A = [list_data[n][1] for n in range(N)]
    return N, S, A

sol = -1
# 입력받는 부분
N, S, A = Input_Data()

# 여기서부터 작성
for student, apple in zip(S,A):
    sol += apple%student

# 출력하는 부분
print(sol+1)