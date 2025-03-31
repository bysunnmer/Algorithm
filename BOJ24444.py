# 25.03.31

N, M, R = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    arr[u][v] = arr[v][u] = 1
    