# 25.03.25

N, M = map(int, input().split())
path = []


def perm(start):
    if len(path) == M:
        print(*path)
        return

    for i in range(start, N+1):
        path.append(i)
        perm(i)
        path.pop()


perm(1)