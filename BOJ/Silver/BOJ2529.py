# 25.05.18

k = int(input())
lst = list(input().split())
visited = [0] * 10

stack = lst[:]
while stack:
    compare = stack.pop(0)
    for i in range(10):
        now = i
        visited[i] = 1
        if compare == '<':
            for j in range(i+1, 10):
                if visited[j] == 1:
                    continue
                next = j

