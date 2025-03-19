# 25.03.19

# 호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방 선호
# W 개의 방이 있는 H 층 건물
# 방번호 YXX 또는 YYXX

T = int(input())
for tc in range(T):
    H, W, N = map(int, input().split())
    cnt = 0
    Y = X = 0
    for c in range(1, W+1):
        for r in range(1, H+1):
            cnt += 1
            if cnt == N:
                Y = r
                X = c
                break
    print(Y, end="")
    print("{:02}".format(X))