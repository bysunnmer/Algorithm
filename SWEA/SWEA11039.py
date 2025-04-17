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


# >>> pass 하긴 했는데 다른 방법으로 다시 풀기
# 완전탐색

def get_sum(r1, c1, h, w):
    r2, c2 = r1 + h - 1, c1 + w - 1
    total = psum[r2][c2]
    if r1 > 0:
        total -= psum[r1-1][c2]
    if c1 > 0:
        total -= psum[r1][c1-1]
    if r1 > 0 and c1 > 0:
        total += psum[r1-1][c1-1]
    return total


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    psum = [[0] * N for _ in range(N)]
    max_v = 0

    for i in range(N):
        for j in range(N):
            psum[i][j] = arr[i][j]
            if i > 0:
                psum[i][j] += psum[i-1][j]
            if j > 0:
                psum[i][j] += psum[i][j-1]
            if i > 0 and j > 0:
                psum[i][j] -= psum[i-1][j-1]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                for h in range(1, N-r+1):
                    for w in range(1, N-c+1):
                        if r+h >= N or c+w >= N:
                            continue
                        if get_sum(r, c, h, w) == h * w:
                            max_v = max(max_v, h * w)
    print(max_v)