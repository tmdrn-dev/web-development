'''
입력 설명
각 역에서 내린 사람 수(0 이상, 10000 이하)와 탄 사람 수(0 이상, 10000 이하)가 빈칸을 사이에 두고 첫째 줄부터 넷째 줄까지 역 순서대로 한 줄에 하나씩 주어진다.
0 32
3 13
28 25
39 0
출력 설명
첫째 줄에 최대 사람 수를 출력한다.
42
'''

import sys

sol = 0
people = 0
for _ in range(4):
    off, on = map(int, sys.stdin.readline().split())
    people = people - off + on
    if sol < people:
        sol = people

print(sol)
