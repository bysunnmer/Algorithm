# 25.03.27

N = int(input())


def check(row, col):
    # 이 전에 선택한 열과 같은 열이면 return
    for i in range(row):
        if visited[i][col] == 1:
            return False

    # 오른쪽 대각선 상에 있으면 return
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if visited[i][j] == 1:
           return False
        i -= 1
        j += 1

    # 왼쪽 대각선 상에 있으면 return
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if visited[i][j] == 1:
            return False
        i -= 1
        j -= 1

    return True


def dfs(row):
    global cnt

    if row == N:
        cnt += 1
        return

    for c in range(N):
        if check(row, c):
            visited[row][c] = 1
            dfs(row+1)
            visited[row][c] = 0

visited = [[0] * N for _ in range(N)]
cnt = 0

dfs(0)

print(cnt)