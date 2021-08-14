'''
[입력 설명]
첫 줄에 N(3<= N <= 100), M(1<= M <= N)을 입력 받는다.
N은 지하철역의 수, M은 원하는 목적역의 번호를 입력 받는다.
둘째 줄부터 N개의 줄이 나오고, 각 줄에는 N개의 수 S가 입력된다.
i번째 줄에서 j번째 수 Sij는 i번 역에서 j번 역까지 가는데 걸리는 시간이다.
1번 역이 숙소가 있는 역이고, Sij에서 i=j 일 때는 항상 0이다. (0<= S <=100)
5 5
0 2 2 5 9
2 0 3 4 8
2 3 0 7 6
5 4 7 0 5
9 5 6 5 0
[출력 설명]
목적 역까지 가는데 걸리는 최소 시간과 최소시간으로 가는 최단 경로를 출력한다.
8
1 3 5
'''

N, M  = map(int, input().split())
a = [list(map(int, input().split())) for i in range(N)]

def bfs():
    que = []
    visit = [100 * N + 1 for _ in range(0,N)]
    path =  [0 for _ in range(0,N)]

    

    que.append(0)
    path[0] = 0
    visit[0] = 0
    while(len(que)):
        cur = que.pop(0)
        for e in range(0, N):
            
            if visit[e] <= visit[cur]+a[cur][e]: 
                continue
            que.append(e)
            visit[e] = visit[cur] + a[cur][e]
            path[e] = cur
            print('visit', visit)
            print('path', path)
    return path, visit

def prt(m):
    if m == 0: return
    prt(path[m])
    print(m+1, end = ' ')

path, visit = bfs()
print(visit[M-1])
print('1', end=' ' )
prt(M-1)