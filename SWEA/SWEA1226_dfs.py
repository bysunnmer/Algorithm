#25.04.12


def dfs(y, x):
    global result
    visited[y][x] = 1

    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = y + dy, x + dx
        if arr[ny][nx] == 3:
            result = 1
        if ny < 1 or ny >= 14 or nx <1 or ny >= 14:
            continue
        if arr[ny][nx] == 1 or visited[ny][nx] == 1:
            continue
        dfs(ny, nx)


T = 10
for _ in range(T):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    result = 0

    dfs(1, 1)

    print(f'#{tc} {result}')