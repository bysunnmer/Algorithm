# 25.03.18

N, M = map(int, input().split())
path = []
used = [0] * (N+1)

def comb(cnt):
    if cnt == M:
        print(*path)
    for i in range(1, N+1):
        if used[i] != 0:
            continue
        used[i] = 1
        path.append(i)
        comb(cnt+1)
        path.pop()
        used[i] = 0

comb(0)