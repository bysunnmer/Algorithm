# 25.03.29

N = 8
visited = [0] * N
cnt = 0


def check(row):
    for r in range(row):
        if visited[row] == visited[r]:
            return False
        if abs(visited[row] - visited[r]) == abs(row - r):
            return False

    return True


def queen(row):
    global cnt

    if row == N:
        cnt += 1
        return

    for col in range(N):
        visited[row] = col
        if not check(row):
            continue
        queen(row+1)
        visited[row] = 0        # 초기화 안 해도 됨


queen(0)
print(cnt)