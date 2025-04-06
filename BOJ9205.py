# 25.04.06

# 상근이 집에서 맥주 한 박스 (20개) 들고 출발
# 50미터에 한 병 씩
# 편의점에서 빈 병 버리고 새 맥주 병 살 수 있음
# 박스에 들어있는 맥주는 20병 넘을 수 없음
# 편의점 나선 직후에도 50미터 가기 전에 맥주 한 병 마셔야 됨

from collections import deque

t = int(input())
for tc in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    con = [list(map(int, input().split())) for _ in range(n)]
    fx, fy = map(int, input().split())
    lst = con + [fx, fy]
    visited = [0] * (n+1)

    q = deque()



    def bfs():

        for i in range(len(lst)):
            if visited[i]:
                continue
            elif abs(lst):
                visited[i] = 1
                q.append(con[i])


    flag = False
    first = abs(con[0][0] - hx) + (con[0][1] - hy)  # 1000
    if first <= 20 * 50:
        drink = 20 - first // 50
        buy = drink

        second = abs(con[1][0] - con[0][0]) + abs(con[1][1] - con[0][1])
        if second <= 20 * 50:
            drink = 20 - second // 50
            buy = drink

            third = abs(con[1][0] - fx) + abs(con[1][1] - fy)
            if third <= 20 * 50:
                flag = True

    if flag:
        print('happy')
    else:
        print('sad')