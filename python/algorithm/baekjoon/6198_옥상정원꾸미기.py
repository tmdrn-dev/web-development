size = int(input())
array = [int(input()) for _ in range(size)]

lookatme = 0
stack = list()
for i in range(size):
    if not stack:
        lookatme += len(stack)
        stack.append(array[i])
    else:
        while stack:
            if stack[-1] <= array[i]:
                stack.pop()
            else:
                break
        lookatme += len(stack)
        stack.append(array[i])

print(lookatme)
