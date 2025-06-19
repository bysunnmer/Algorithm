# 25.06.19

N = int(input())

def each(number):
    return sum(map(int, str(number)))

answer = 0
for n in range(1, N):       # start 를 max(1, N - 9 * len(str(N))) 로 하면 탐색 범위 줄일 수 있음
    dsum = n + each(n)
    if dsum == N:
        answer = n
        break

print(answer)