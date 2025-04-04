# 25.04.04

def dfs(v):
    global cnt

    visited[v] = 1
    cnt += 1
    arr[v].sort()
    for n in arr[v]:
        if visited[n] == 1:
            continue
        dfs(n)
    return cnt

N, M, R = map(int, input().split())
arr = [] * (N + 1)
visited = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

cnt = 0
dfs(R)