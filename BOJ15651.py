# 25.03.24

N, M = map(int, input().split())
path = []


def perm(cnt):
    if cnt == M:
        print(*path)
        return

    for i in range(1, N+1):
        path.append(i)
        perm(cnt + 1)
        path.pop()


perm(0)
