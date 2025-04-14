# 25.04.14

visited = [[0]*101 for _ in range(101)]
for _ in range(4):
    lx, ly, rx, ry = map(int, input().split())
    for r in range(ly+1, ry+1):
        for c in range(lx+1, rx+1):
            visited[r][c] = 1

cnt = 0
for i in range(101):
    for j in range(101):
        if visited[i][j] == 1:
            cnt += 1

print(cnt)