'''
입력 설명
첫 줄에 영화의 수 N이 입력된다. (3<=N<=100,000)
둘째 줄부터 N개의 줄에 영화 시작시간과 종료시간이 공백으로 구분되어 입력된다.
(1<=시간<=100,000,000) 종료시간이 시작시간보다 크다.
5
1 3
2 5
8 10
4 7
6 9
출력 설명
관람할 수 있는 최대 영화의 수를 출력하라.
3
'''

N = int(input())
data = []
for _ in range(0, N):
    s, e = map(int,input().split())
    data.append((e, s))
    
data = sorted(data)

sol = 0
time = data[0][0]
for e, s in data:
    if s > time:
        time = e
        sol+=1

print(sol+1)
