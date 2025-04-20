# 25.04.20

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    rocks = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())

        for k in range(1, j+1):
            if i-1-k < 0 or i-1+k >= N:
                break
            if rocks[i-1-k] == rocks[i-1+k]:
                rocks[i-1-k] = 1 - rocks[i-1-k]
                rocks[i-1+k] = 1 - rocks[i-1+k]

    print(f'#{tc}', *rocks)