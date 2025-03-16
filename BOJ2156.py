# 25.03.16

# 포도주 잔 선택하면 그 잔에 들어있는 포도주는 모두 마시고 원래 위치에 다시 놓아야 됨
# 연속으로 놓인 세 잔을 모두 마실 수 없음
# 최대한 많은 양의 포도주 맛보고 싶은 효주

n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0] * n

if n >= 1:      # n의 범위 지정 안 해주면 인덱스 에러 남
    dp[0] = arr[0]
if n >= 2:
    dp[1] = dp[0] + arr[1]
if n >= 3:
    dp[2] = max(dp[0] + arr[2], dp[1], arr[1] + arr[2])

if n >= 4:
    for i in range(3, n):
        dp[i] = max(dp[i-2] + arr[i], arr[i] + arr[i-1] + dp[i-3], dp[i-1])

print(dp[n-1])