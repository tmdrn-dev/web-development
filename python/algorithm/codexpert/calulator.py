'''
[입력 설명]
첫 줄에 정수의 개수 N이 입력으로 주어진다.
둘째 줄에는 N개의 정수 M과 연산자로 구성 된 수식이 주어진다. 정수와 연산자 사이에는 공백이 하나 주어진다. (1≤ N ≤20, 1≤ M ≤10 , 연산자 - +, -, *, / )
4
1 - 4 * 9 + 10
[출력 설명]
수식의 연산결과를 출력한다.
-25
'''
import sys
from collections import deque
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    str_exp = readl().split()
    nums = deque(map(int,str_exp[0::2]))
    op = deque(str_exp[1::2])
    return N, nums, op

sol = -1
# 입력받는 부분
N, nums, op = Input_Data()

result = list()
# 여기서부터 작성

num = nums.popleft()
result.append(num)
while op:
    o = op.popleft()
    if o == '-':
        num = nums.popleft()
        result.append(-1*num)
    elif o == '*':
        left = result.pop()
        right = nums.popleft()
        result.append(right*left)
    elif o == '/':
        left = result.pop()
        right = nums.popleft()
        result.append(int(left/right))
    elif o == '+':
        num = nums.popleft()
        result.append(num)

for i in result:
    sol += i
print(sol+1)
