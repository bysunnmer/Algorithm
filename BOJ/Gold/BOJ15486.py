# 25.04.27 / 25.04.29

# 오늘부터 N+1 일 째 되는 날 퇴사, N일 남음

N = int(input())
lst = [(0, 0)]
l_idx = -1
for i in range(N):
    T, P = map(int, input().split())
    lst.append((T, P))
    if i+T <= N:
        l_idx = i+1

dp = [0] * (N+1)
dp[l_idx] = lst[l_idx][1]
m_idx = l_idx

for d in range(l_idx-1, 0, -1):
    # if d + lst[d][0] <= m_idx:
    #     dp[d] = dp[d+1] + lst[d][1]
    #     m_idx = d
    # else:
        dp[d] = max(dp[d+1], lst[d][1] + dp[d+lst[d][0]])
        # if dp[d] == lst[d][1]:
        #     m_idx = d
print(dp[1])


# dp 아님
# max_b = 0
# for d in range(1, l_idx+1):
#     benefit = 0
#     day = d
#
#     while day <= N and day + lst[day][0] <= N+1:
#         benefit += lst[day][1]
#         n_day = lst[day][0]
#         day += n_day
#     max_b = max(benefit, max_b)

    # for n in range(n_day, l_idx+1):
    #     b = 0
    #     future = n
    #     while True:
    #         b += lst[future][1]
    #         future += lst[future][0]
    #         if future > N or future + lst[future][0] > N+1:
    #             break
    #     max_b = max(benefit+b, max_b)
    #     print(f'{d} 이고 {n} 일때 {future} , {max_b}')

# print(max_b)