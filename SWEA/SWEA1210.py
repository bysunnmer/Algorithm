# 25.04.20

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    end_x = -1

    for x in range(100):
        if ladder[99][x] == 2:
            end_x = x

    r = 99
    c = end_x
    while r > 0:
        for dr, dc in [(0, -1), (0, 1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if nc < 0 or nc >= 100:
                continue
            if ladder[nr][nc] != 1:
                continue
            ladder[r][c] = 3
            r, c = nr, nc
            break

    print(f'#{tc} {c}')

