# 25.04.16
# from collections import deque
#
# def bfs(x, y):
#     cnt = 1
#     visited[x][y] = 1
#     q.append((x, y))
#
#     while q:
#         r, c = q.popleft()
#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             nr, nc = r + dr, c + dc
#             if nr < 0 or nr >= N or nc < 0 or nc >= N:
#                 continue
#             if visited[nr][nc] == 1:
#                 continue
#             if arr[nr][nc] == 1:
#                 visited[nr][nc] = 1
#                 cnt += 1
#                 q.append((nr, nc))
#
#     return cnt
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     q = deque()
#     max_v = 0
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 1 and visited[i][j] == 0:
#                 temp = bfs(i, j)
#                 max_v = max(max_v, temp)
#
#     print(f'#{tc} {max_v}')


# >>> pass 하긴 했는데 더 효율적인 방법으로 다시 풀기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]