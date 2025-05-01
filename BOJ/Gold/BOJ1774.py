# 25.05.01
from math import sqrt

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    ref_x = find(x)
    ref_y = find(y)

    if ref_x == ref_y:      # 초기 주어지는 연결된 통로들 확인하기 위해서 필요
        return False

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y
    return True

N, M = map(int, input().split())

position = [(0, 0)]
for _ in range(N):
    X, Y = map(int, input().split())
    position.append((X, Y))

parents = [i for i in range(N+1)]
edges = []
cnt = 0
length = 0
init = 0

for _ in range(M):
    a, b = map(int, input().split())
    if union(a, b):         # 임의로 parents 수정하면 안 되고 union 에 넣어서 부모노드 찾아야 됨
        init += 1           # 이미 입력 중에 연결되는 경우도 있어서 union 을 통해 연결된 개수를 세고 N-1 에서 해당 수를 빼야 총 간선의 수

for i in range(1, N):
    for j in range(i+1, N+1):
        edges.append((i, j, sqrt(((position[i][0] - position[j][0]) ** 2) + (position[i][1] - position[j][1]) ** 2)))

edges.sort(key=lambda x: x[2])

for x, y, d in edges:
    if find(x) == find(y):
        continue
    union(x, y)
    cnt += 1
    length += d

    if cnt == N - init - 1:
        break

answer = round(length, 2)
print("%.2f" %answer)