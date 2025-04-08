# 25.04.08

# 음식의 신맛은 사용한 재료의 신맛의 곱, 쓴맛은 합
# 신맛과 쓴맛의 차이를 작게 만들어라
# 재료는 적어도 하나 사용
# 신맛과 쓴맛의 차이가 가장 작을 때를 출력


def comb(cnt, path):

    if cnt == len(tastes):
        if path:
            result.append(path)
        return

    comb(cnt + 1, path)
    comb(cnt + 1, path + [cnt])
    return


def cook(lst):
    global min_v

    S = 1
    B = 0
    for l in lst:

        S *= tastes[l][0]
        B += tastes[l][1]

        min_v = min(abs(S-B), min_v)


N = int(input())
tastes = [list(map(int, input().split())) for _ in range(N)]
path = []
result = []
min_v = float('inf')


comb(0, [])

for r in result:
    cook(r)

print(min_v)