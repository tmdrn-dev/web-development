'''
[입력 설명]
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
[출력 설명]
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지 내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
3
7
8
9
'''
N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

count = 0
def dfs(row, col, n):
    global count
    visited[row][col] = n
    count += 1

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if (-1 < nr and nr < N) and (-1 < nc and nc < N):
            if visited[nr][nc] == 0 and matrix[nr][nc] == 1:
                dfs(nr, nc, n)

apt = list()
numbering = 1
for row in range(N):
    for col in range(N):
        if visited[row][col] == 0 and matrix[row][col] == 1:
            dfs(row, col, numbering)
            apt.append(count)
            numbering += 1
            count = 0

print(len(apt))
for i in sorted(apt):
    print(i)