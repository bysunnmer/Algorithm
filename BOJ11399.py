# 25.03.28

# ATM 1대 있는데 N명이 줄 서 있음
# i번 사람이 돈을 인출하는 데 걸리는 시간은 Pi분
# 줄 서는 순서에 따라 돈 인출에 필요한 시간의 합이 달라짐
# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값 구하기

N = int(input())
P = list(map(int, input().split()))

P.sort()

min_s = temp = 0
for i in range(N):
    temp += P[i]
    min_s += temp

print(min_s)