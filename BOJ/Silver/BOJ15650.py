# 25.03.20

N, M = map(int, input().split())
path = []

def perm(cnt, idx):
    if cnt == M:
        path.sort()
        print(*path)

    for i in range(idx, N+1):
        path.append(i)
        perm(cnt+1, i+1)
        path.pop()

    return path


perm(0, 1)