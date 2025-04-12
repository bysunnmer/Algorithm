# 25.03.29

# 모인 사람은 N명 (짝수)
# N//2 명으로 이루어진 두 팀으로 나누기
# 능력치 차이의 최솟값 출력

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
result = float('inf')


def comb(idx, cnt):
    global result
    s_sum = l_sum = 0

    if cnt == N//2:
        for i in range(N):
            for j in range(N):
                if visited[i] == visited[j] == 1:
                    s_sum += S[i][j]
                elif visited[i] == visited[j] == 0:
                    l_sum += S[i][j]
        temp = abs(s_sum - l_sum)
        if result > temp:
            result = temp
        return

    for i in range(idx, N):
        if not visited[i]:      # 팀을 두개로 나누는 방법의 핵심
            visited[i] = 1
            comb(i+1, cnt+1)
            visited[i] = 0


comb(0, 0)
print(result)