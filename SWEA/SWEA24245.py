# 25.03.20

# 이긴 경우 -> 전 패를 그대로 유지
# 진 경우 -> 상대방의 패를 이기는 패로 변경
# 무승부 -> 현재 패를 그대로
# 가위 1 바위 2 보 3

T = int(input())
for tc in range(1, T+1):
    tak, o = map(int, input().split())
    if [tak, o] in [[1, 3], [2, 1], [3, 2]]:
        result = tak
    elif tak == o:
        result = tak
    else:
        if o == 1:
            result = 2
        elif o == 2:
            result = 3
        else:
            result = 1

    print(f'#{tc} {result}')