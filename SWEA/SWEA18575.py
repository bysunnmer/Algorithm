# 25.04.20

def pang(r, c):
    score = sum(arr[r])
    for row in range(N):
        if row == r:
            continue
        score += arr[row][c]

    return score


# 열의 합 계산 하기
# col_sums = [sum(col) for col in zip(*MAP)]
# print(col_sums)   # [1+4+7, 2+5+8, 3+6+9] → [12, 15, 18]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 360
    max_v = 0

    for i in range(N):
        for j in range(N):
            temp = pang(i, j)
            min_v = min(min_v, temp)
            max_v = max(max_v, temp)

    result = max_v - min_v
    print(f'#{tc} {result}')