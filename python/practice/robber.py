'''
100 5
10 5
30 2
40 4
90 1
70 2
'''
import sys
read = sys.stdin.readline

W, N = map(int, read().split())
MP = dict()

for _ in range(N):
    M, P = map(int, read().split())
    if P not in MP.keys():
        MP[P] = M
    else:
        MP[P] += M

MP = sorted(MP.items(), reverse=True)
#print(MP)

price = 0
for P, M in MP:
    if W == 0:
        break
    else:
        if W >= M:
            price += M*P
            W -= M
        else:
            price += W*P
            W = 0

print(price)