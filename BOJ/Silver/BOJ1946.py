# 25.05.11

T = int(input())
for tc in range(T):

    N = int(input())
    rank = [list(map(int, input().split())) for _ in range(N)]

    rank.sort(key=lambda x:(x[0], x[1]))
    print(rank)
    # for i in range(len(rank)):
    #     rank[i][0]
