# 25.08.21

N = int(input())

limit = 1
cnt = 1

while N > limit:
    limit += cnt * 6
    cnt += 1

print(cnt)