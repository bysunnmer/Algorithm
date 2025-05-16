# 25.05.11 / 25.05.16
import sys
input = sys.stdin.readline


T = int(input())
for tc in range(T):

    N = int(input())
    rank = [list(map(int, input().split())) for _ in range(N)]

    rank.sort(key=lambda x:(x[0], x[1]))
    # print(rank)

    # 한 지원자의 서류 성적을 다른 지원자들이랑 비교
    # 어떤 지원자보다 성적 순위가 낮은 경우 (큰 숫자) 그 둘의 면접 순위 비교
    # cnt = N
    # for i in range(N):
    #     for j in range(i):
    #         # if i == j:
    #         #     continue
    #         # if rank[i][0] < rank[j][0]:
    #         #     continue
    #         if rank[i][1] < rank[j][1]:
    #             continue
    #         cnt -= 1
    #         break

    # print(cnt)

    # 이미 서류 순으로는 정렬 했으니까 정렬된 순서대로 면접 성적을 비교해서
    # 현재 지원자의 면접 순위가 이전보다 높을 경우 (작은 숫자) 합격 가능
    # 합격 가능한 지원자의 순위를 best 로 계속 갱신
    
    cnt = N
    best = N
    for i in range(N):
        if rank[i][1] <= best:
            best = rank[i][1]
            continue
        cnt -= 1
    print(cnt)

