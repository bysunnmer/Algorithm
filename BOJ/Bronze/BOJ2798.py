# 25.08.22

# def comb(arr, result, answer, start):
#     if len(result) == 3:
#         answer.append(result)
#         return
#
#     for i in range(start + 1, len(arr)):
#         comb(arr, result + [arr[i]], answer, i)
#     return answer
#
# N, M = map(int, input().split())
# card = list(map(int, input().split()))
# mx = 0
# ans = comb(card, [], [], 0)
# for a in ans:
#     if sum(a) <= M:
#         mx = max(mx, sum(a))
#
# print(mx)

#
#
#

# itertools 방법

# from itertools import combinations
#
# N, M = map(int, input().split())
# card = list(map(int, input().split()))
#
# m_sum = 0
# for c in combinations(cards, 3):
#     if sum(c) <= M:
#         m_sum = max(m_sum, sum(c))
#
# print(m_sum)

#
#
#

# dfs 방법

def dfs(start, total, cnt):
    global s_max

    if total > M:
        return

    if cnt == 3:
        s_max = max(s_max, total)
        return

    for i in range(start, N):
        dfs(i+1, total+card[i], cnt+1)


N, M = map(int, input().split())
card = list(map(int, input().split()))
s_max = 0

dfs(0, 0, 0)

print(s_max)