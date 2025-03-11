# 25.03.11

def dfs(v, cnt):
  visited[v] = 1

  for c in range(C+1):
    if arr[v][c] == 1 and visited[c] != 1:
      cnt = dfs(c, cnt+1)
  return cnt

C = int(input())
N = int(input())
arr = [[0]*(C+1) for _ in range(C+1)]
visited = [0]*(C+1)
for _ in range(N):
  a, b = map(int, input().split())
  arr[a][b] = arr[b][a] = 1

print(dfs(1, 0))