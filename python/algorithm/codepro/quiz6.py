# https://codepro.lge.com/exam/18/%EA%B5%AD%EB%82%B4-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C/quiz/6

'''
1. matrix를 n**2로 순회해도 최대 O(100)이므로 시간은 큰 제약 사항이 아님
2. 나를 '덧씌운' 색을 list up해서 사용된 색에서 제거하는 방식으로 계산
3. 나의 영역을 순회하며 다른 색이 바견되면 나를 '덧씌운 색'임
'''

from sys import stdin
read = stdin.readline

size = int(input())
canvas = [list(map(int, input())) for _ in range(size)]

color_num = 10
color_set = dict()
for i in range(color_num):
    color_set[i] = [[] for _ in range(2)]

for i, row in enumerate(canvas):
    for j, color in enumerate(row):
        color_set[color][0].append(i)
        color_set[color][1].append(j)

used_color = 0
overwrite = dict()
for color in range(1, color_num):
    if not color_set[color][0]:
        continue

    used_color += 1
    colori = sorted(color_set[color][0])
    colorj = sorted(color_set[color][1])

    #print('color:{}, i:{}~{}, j:{}~{}'.format(color, colori[0], colori[-1], colorj[0], colorj[-1]))

    for i in range(colori[0], colori[-1]+1):
        for j in range(colorj[0], colorj[-1]+1):
            if canvas[i][j] != color:
                overwrite[canvas[i][j]] = True

print(used_color - len(overwrite))
