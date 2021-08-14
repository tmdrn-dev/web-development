'''
입력 설명
첫 줄에 주사위를 던진 횟수 N(2≤N≤5)과 출력모양 M(1≤M≤3)이 들어온다.
3 1
출력 설명
주사위를 던진 횟수 N에 대한 출력모양을 출력한다.
작은 숫자부터 출력한다.
1 1 1
1 1 2
1 1 3
1 1 4
1 1 5
1 1 6
1 2 1
…
6 6 6
'''

import sys
N, M = map(int, sys.stdin.readline().split())

dice = [1,2,3,4,5,6]

if M==1:
    from itertools import product
    for i in product(dice, repeat=N):
        print(*i)
elif M==2:
    from itertools import combinations_with_replacement
    for i in combinations_with_replacement(dice, N):
        print(*i)
else:
    from itertools import permutations
    for i in permutations(dice, N):
        print(*i)
