# 25.04.16
from collections import deque

def bfs(x, y):
    cnt = 1
    q.append((x, y))
    r, c = q.popleft()

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
       nr, nc = r + dr, c + dc
       if nr < 0 or nr >= N or nc < 0 or nc >= N:
           continue
        if visited[nr][nc] == 1:
            continue
        visited[nr][nc] = 1
        cnt += 1
        q.append((nr, nc))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    q = deque()




    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                bfs(i, j)