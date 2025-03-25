# 25.03.24

T = int(input())
for tc in range(T):
    arr = list(input())
    cnt = 0
    result = 0
    for p in range(len(arr)):
        if arr[p] == "O":
            cnt += 1
            result += cnt
        else:
            cnt = 0
            result += cnt

    print(result)