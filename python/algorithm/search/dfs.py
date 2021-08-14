# stack과 recursion으로 가능
# https://kingpodo.tistory.com/47?category=805745

graph = [
[0,1,1,1,0,0,0], #0
[1,0,0,0,1,0,0], #1
[1,0,0,0,1,1,0], #2
[1,0,0,0,0,1,0], #3
[0,1,1,0,0,0,1], #4
[0,0,1,1,0,0,1], #5
[0,0,0,0,1,1,0]] #6

row = len(graph)
column = len(graph[0])

visited = [False] * column

# 재귀 함수로 구현하기
# def dfs(graph, node, visited):
#     visited[node] = True
#     print(node)
    
#     for i in range(column):
#         if graph[node][i] is 1 and visited[i] is False:
#             dfs(graph, i, visited)

# 스택으로 구현하기
# visited[] 배열을 보면 모든 정점의 방문 여부를 false로하여 방문하지 않은 것을 하며 stack[]에는 순회를 시작할 정점를 넣어줍니다.
# stack[]을 pop하여 0을 삭제하여 0정점을 방문하고 visited[0]을 true로 바꾸어 줍니다.
# 이 부분 중요!!! 정점 0과 인접한 모든 인접 노드 중 방문하지 않은 노드를 stack[]에 push합니다.
# stack[]을 pop하여 1을 삭제하여 1정점을 방문하고 visited[1]을 true로 바꾸어 줍니다. 
# ...
# 모든 정점을 방문한 상태에서 스택에 데이터가 남아있는경우 나머지 데이터들도 pop하지만 visited[]배열에 방문하지 않은 정점이 없기 때문에 계속 pop연산만하고 모든 데이터가 pop이되면 종료가 됩니다. 

def dfs(graph, root, visited):
    stack = [root]
    while stack:
        node = stack.pop()
        if visited[node] is False:
            print(node)
            visited[node] = True

        for i in reversed(range(row)):
            if graph[node][i] is 1 and visited[i] is False:
                stack.append(i)

dfs(graph, 0, visited)
