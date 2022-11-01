import bisect
import sys
read = sys.stdin.readline

'''
5
3 2 4 5 1
'''

N = int(read())
A = list(map(int, read().split()))

def count_rocks(array, reverse=False):
    if reverse == True:
        array.reverse()

    visited = list()
    counts = [1 for _ in range(N)]

    for i, height in enumerate(array):
        if i == 0:
            visited.append(height)
        else:
            if visited[-1] < height:
                visited.append(height)
                counts[i] = len(visited)
            else:
                idx = bisect.bisect_left(visited, height)
                visited[idx] = height

    if reverse == True:
        counts.reverse()
    return counts

increase = count_rocks(A)
decrease = count_rocks(A, True)
# print(increase)
# print(decrease)

result = [*zip(increase, decrease)]
ans = 0
for res in result:
    inc, dec = res
    ans = max(ans, inc+dec)

print(ans -1)