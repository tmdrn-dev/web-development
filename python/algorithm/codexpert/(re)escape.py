'''
입력 설명
첫 줄에 소들의 수 N(1≤N≤20)이 주어진다.
두 번째 줄부터 N 줄에 걸쳐 각 소의 무게(W_i)가 입력된다. (정수, 1≤W_i≤100,000,000)
5
522
6
84
7311
19
출력 설명
무게를 모두 더했을 때 어떤 자리에서도 자리올림이 발생하지 않는 소들의 최대 수를 출력하라.
3
'''
#아래는 정답이지만 내가 푼 것은 아님

import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    weight = [int(readl()) for _ in range(N)]
    return N, weight


def check(a, b):
    while a and b:
        if a%10 + b%10 > 9:
            return False
        a //= 10
        b //= 10
    return True


def dfs(s, cnt, sum_weight):
    global sol
    if cnt + (N-s) <= sol:
        return
    sol = max(sol, cnt)
    for n in range(s, N):
        if check(sum_weight, weight[n]):
            dfs(n+1, cnt+1, sum_weight+weight[n])


sol = -1
# 입력받는 부분
N, weight = input_data()

# 여기서부터 작성
sol = 0
dfs(0, 0, 0)

# 출력하는 부분
print(sol)