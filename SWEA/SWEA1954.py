# 25.04.15

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    num = 0
    r = c = 0
    nr = nc = 0
    direction = 0
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while True:
        num += 1
        arr[r][c] = num
        if num == N*N:      # 이걸 while 조건으로 할 걸
            break
        nr = r + delta[direction][0]
        nc = c + delta[direction][1]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            r, c = nr, nc
            continue
        else:
            direction = (direction + 1) % 4
            nr = r + delta[direction][0]
            nc = c + delta[direction][1]
            r, c = nr, nc
            continue

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])