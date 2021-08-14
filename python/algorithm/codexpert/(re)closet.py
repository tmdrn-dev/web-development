'''
[입력 설명]
입력의 첫 번째 줄에 벽장의 개수를 나타내는 2보다 크고 20보다 작거나 같은 하나의 정수, 두 번째 줄에 초기에 열려있는 두 개의 벽장을 나타내는 두 개의 정수, 
그리고 세 번째줄에는 사용할 벽장들의 순서의 길이(최대 20), 그리고 그 다음줄부터 사용할 벽장의 번호가 한줄에 하나씩 순서대로 주어진다.
7
2 5
4
3
1
6
5
[출력 설명]
벽장문의 최소 이동횟수를 화면에 출력한다.
5
'''
# 아래 코드는 정답이지만 내가 짠 코드는 아님
import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    door_f, door_r = map(int, readl().split())
    seq = [int(readl()) for _ in range(int(input()))]
    return N, door_f, door_r, seq

def solve(door, n, o1, o2, cnt_move):
    global sol
    print(door, 'n', n, 'f', o1, 'r', o2, 'sol', sol, 'cnt', cnt_move)
    if n >= len(seq):
        sol = cnt_move
        return

    if sol > cnt_move + abs(o1-seq[n]):
        solve('door_f', n+1, seq[n], o2, cnt_move + abs(o1-seq[n]))
    
    if sol > cnt_move + abs(o2-seq[n]):
        solve('door_r', n+1, o1, seq[n], cnt_move + abs(o2-seq[n]))

sol = -1

#입력받는 부분
N, door_f, door_r, seq = input_data()

# 여기서부터 작성
sol = 100000000
solve('', 0, door_f, door_r, 0)

# 출력하는 부분
print(sol)