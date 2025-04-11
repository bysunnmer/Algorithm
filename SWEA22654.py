# 25.04.10

# 필드의 정보 = G, T, X, Y
# 동작 = A, L, R
# 차윤이는 RC 카를 항상 위를 바라보는 방향으로부터 조종 시작
# 커맨드로 목적지에 도달할 수 있는지!!


def move(cur_com):
    global direction, cr, cc

    if cur_com == "A":
        dr, dc = delta[direction]
        nr, nc = cr + dr, cc + dc

        if nr < 0 or nr >= N or nc < 0 or nc >= N or field[nr][nc] == "T":
            return
        else:
            # field[xr][xc] = "G"
            # field[nr][nc] = "X"
            cr, cc = nr, nc

    elif cur_com == "L":
        direction = (direction - 1) % 4
    elif cur_com == "R":
        direction = (direction + 1) % 4


T = int(input())
for tc in range(1, T+1):
    N = int(input())                                    # 필드의 크기
    field = [list(input()) for _ in range(N)]
    Q = int(input())                                    # 조종 횟수
    command = [list(input().split()) for _ in range(Q)]

    delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    xr = xc = -1
    yr = yc = -1
    result = []

    # 현재 위치 X, 목적지 Y 기억해두기
    for r in range(N):
        for c in range(N):
            if field[r][c] == "X":
                xr = r
                xc = c
            if field[r][c] == "Y":
                yr = r
                yc = c

    # 위치랑 방향은 계속 기억해야할 듯
    # 커맨드에 따라 ALR 수행
    for C, com in command:
        cr, cc = xr, xc
        direction = 0     # 상우하좌 방향을 0123 으로 갱신해보자
        for c in com:
            move(c)
        # 수행이 끝났을 때 X 좌표가 Y 좌표랑 같으면 return 1 아니면 return 0
        if cr == yr and cc == yc:
            result.append(1)
        else:
            result.append(0)

    print(f'#{tc}', *result)


