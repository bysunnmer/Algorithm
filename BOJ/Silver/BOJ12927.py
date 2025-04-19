# 25.04.19

# i번 스위치는 i의 배수 번호를 가지는 전구의 상태를 모두 반전시킴

bulb = list(input())
n = len(bulb)
idx = 0
cnt = 0

while idx < n:
    if bulb[idx] == "Y":
        for i in range(idx, n):
            if (i+1) % (idx+1) == 0:
                if bulb[i] == "Y":
                    bulb[i] = "N"
                else:
                    bulb[i] = "Y"
        cnt += 1
    idx += 1

print(cnt)

