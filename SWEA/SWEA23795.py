# 25.04.17

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                visited[i][j] = 1
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i+di, j+dj
                    while 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == 1:
                            break
                        visited[ni][nj] = 1
                        ni += di
                        nj += dj
                break

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0 and visited[i][j] == 0:
                cnt += 1

    # cnt = sum(row.count(0) for row in MAP) 이 방법도 가능!!!

    print(f'#{tc} {cnt}')