from collections import deque
# stack과 recursion으로 가능
# https://kingpodo.tistory.com/47?category=805745

inputValue = [
[0,1,1,1,0,0,0], #0
[1,0,0,0,1,0,0], #1
[1,0,0,0,1,1,0], #2
[1,0,0,0,0,1,0], #3
[0,1,1,0,0,0,1], #4
[0,0,1,1,0,0,1], #5
[0,0,0,0,1,1,0]] #6

graph = dict()
for row in range(len(inputValue)):
    graph[row] = set()

for row in range(len(inputValue)):
    for col in range(len(inputValue[0])):
        if inputValue[row][col] == 1:
            graph[row].add(col)
            graph[col].add(row)

visited = list()
queue = deque()
queue.append(0)

def bfs(node):
    visited.append(node)
    print(node)
    currentNode = queue.popleft()

    for nextNode in graph[currentNode]:
        if nextNode not in visited:
            queue.append(nextNode)

for row in range(len(graph)):
    if row not in visited:
        bfs(row)

print(visited)