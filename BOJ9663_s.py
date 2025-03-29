def check(row):
    for col in range(row):
        if visited[row] == visited[col]:
            return False

        if abs(visited[row] - visited[col]) == abs(row - col):
            return False

    return True


def dfs(row):
    global cnt

    if row == N:
        cnt += 1
        return

    for col in range(N):
        visited[row] = col
        if not check(row):
            continue

        dfs(row + 1)

N = int(input())
visited = [0] * N
cnt = 0

dfs(0)
print(cnt)