'''
[입력 설명]
첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. N은 3 이상 10,000 이하이다.
다음 줄에는 각 지방의 예산요청을 표현하는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 값들은 모두 1 이상 100,000 이하이다.
그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. M은 N이상 1,000,000,000 이하이다.
4
120 110 140 150
485
[출력 설명]
배정된 예산들 중 최대값인 정수를 출력한다.
127
'''

from sys import stdin
read = stdin.readline

N = int(input())
budget = list(map(int, read().split()))
M = int(input())

print(N, budget, M)

budget_sum = 0
for i in budget:
    budget_sum += i

budget_avr = (budget_sum/N)
print(budget_sum)
print(budget_avr)