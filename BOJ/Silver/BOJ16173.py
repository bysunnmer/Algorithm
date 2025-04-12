# 25.03.10

# 정사각형 구역 내부에서만 이동
# 출발점은 항상 정사각형 가장 왼쪽, 가장 위의 칸
# 이동 가능한 방향은 오른쪽과 아래 뿐
# 가장 오른쪽, 가장 아래 칸에 도달하는 순간 쩰리의 승
# 한 번에 이동할 수 있는 칸의 수는 현재 밟고 있는 칸에 쓰여 있는 수 만큼

def dfs(r, c):
  if r == c == N-1:
    return "HaruHaru"
  
  visited[r][c] = 1
  for dr, dc in [[0, 1 * arr[r][c]], [1 * arr[r][c], 0]]:
    nr, nc = r + dr, c + dc
    if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
      if dfs(nr, nc) == "HaruHaru":   # 이 부분 구현 어려웠음
        return "HaruHaru"
  return "Hing"


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
result = dfs(0, 0)
print(result)     # 함수에서는 방문한 곳에 -1 쓰여있으면 방문처리 하고 나오고
                  # 여기서 visited[N-1][N-1] 이 1 인지 확인해서 HaruHaru 나 Hing 출력하는 게 더 간단할 듯