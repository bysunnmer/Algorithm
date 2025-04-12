# 25.03.30

# 한 개의 회의실을 사용하고자 하는 N개의 회의
# 각 회의 I에 대해 시작, 끝 시간 주어짐
# 각 회의가 겹치지 않게 하며 회의실을 사용할 수 있는 회의의 최대 개수 찾기
# 회의의 시작시간과 끝나는 시간이 같을 수도 있음

N = int(input())
I = [list(map(int, input().split())) for _ in range(N)]
I_end = sorted(I, key=lambda x : (x[1], x[0]))
cnt = 1
e = I_end[0][1]
idx = 0

while idx < N:
    for i in range(idx+1, N):
        ns, ne = I_end[i]
        if ns >= e:
            cnt += 1
            e = ne
            idx = i
            break
    else:
        break
print(cnt)
