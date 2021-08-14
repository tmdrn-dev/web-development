'''
[입력 설명]
첫 번째 줄에는 포장 개수 N(1<=N<=5000)이 주어진다.
두 번째 줄에는 포장에 들어있는 사탕의 개수 ni(1<=ni<=100)가 주어진다.
3
2 2 5
[출력 설명]
최소 비용을 출력한다.
13
'''

from sys import stdin
read = stdin.readline

N = int(input())
ni = list(map(int, read().split()))

from collections import deque
package = deque(sorted(ni))

cost = list()
while len(package) > 1:
    left = package.popleft()
    right = package.popleft()
    package.append(left+right)
    cost.append(left+right)
    package = deque(sorted(package))

sol = 0
for i in cost:
    sol += i
print(sol)