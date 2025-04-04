# 25.04.04

# 어떤 배추에 한 마리라도 살고 있으면 인접 다른 배추로 이동해서 그 배추들도 해충 보호 가능
# 인접 배추들이 몇 군데에 있는지 조사하면 몇 마리 필요한 지 알 수 있음

from collections import deque

T = int(input())

def bfs(a, b):
    q = deque()
    q.append((a, b))
    arr[a][b] = 0

    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc] ==0:       # 범위 설정 확인 잘 하기
                continue
            q.append((nr, nc))
            arr[nr][nc] = 0         # 방문처리 했는지 체크 체크 체크 (큐에 넣을 때 하기! 꺼낼 때는 비효율적)

for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    lst = []
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1
        lst.append((Y, X))

    cnt = 0
    for y, x in lst:
        if arr[y][x] == 1:
            bfs(y, x)
            cnt += 1

    print(cnt)


'''
처음 푼 방법도 방문체크만 했으면 시간초과 안 났음

from collections import deque

T = int(input())

def bfs():
    global cnt

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                continue
            q.append((i, j))
            arr[i][j] = 0
            while q:
                r, c = q.popleft()
                for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc] ==0:
                        continue
                    q.append((nr, nc))
                    arr[nr][nc] = 0
            cnt += 1

for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1

    q = deque()
    cnt = 0
    bfs()

    print(cnt)

'''