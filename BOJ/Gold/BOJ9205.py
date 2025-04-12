# 25.04.06 / 25.04.12

# 상근이 집에서 맥주 한 박스 (20개) 들고 출발
# 50미터에 한 병 씩
# 편의점에서 빈 병 버리고 새 맥주 병 살 수 있음
# 박스에 들어있는 맥주는 20병 넘을 수 없음
# 편의점 나선 직후에도 50미터 가기 전에 맥주 한 병 마셔야 됨

from collections import deque


def bfs():
    q.append(0)
    while q:
        idx = q.pop()
        visited[idx] = 1
        for i in range(1, n+2):
            if visited[i]:
                continue
            if abs(places[i][0] - places[idx][0]) + abs(places[i][1] - places[idx][1]) <= 1000:
                if i == n+1:
                    return "happy"
                else:
                    q.append(i)
    return "sad"


t = int(input())
for tc in range(t):
    n = int(input())
    places = []
    for _ in range(n+2):
        x, y = map(int, input().split())
        places.append((x, y))

    visited = [0] * (n+2)
    q = deque()

    result = bfs()

    print(result)