# 25.03.23

# S 에 시작해서 T 에 끝나는 N 개의 수업
# 최소 강의실 사용해서 모든 수업 가능하게
# 수업 끝난 직후에 다음 수업 시작 가능

import heapq

N = int(input())
room = []
pq = []

for i in range(N):
    S, T = map(int, input().split())
    room.append([S, T])
room.sort()

heapq.heappush(pq, room[0][1])
for r in range(1, N):
    if room[r][0] < pq[0]:
        heapq.heappush(pq, room[r][1])
    else:
        heapq.heappop(pq)
        heapq.heappush(pq, room[r][1])

print(len(pq))