# 25.04.22

def bingo(check):
    global l_dia, r_dia

    flag = False
    for i in range(5):
        for j in range(5):
            if board[i][j] == check:
                row[i] += 1
                col[j] += 1
                if i == j:
                    l_dia += 1
                if j == 4 - i:
                    r_dia += 1
                flag = True
                break
        if flag:
            break


board = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]

row = [0] * 5
col = [0] * 5
visited_r = [0] * 5
visited_c = [0] * 5
l_dia = 0
visited_ldia = 0
r_dia = 0
visited_rdia = 0

cnt = 0
result = 0
for r in range(5):
    for c in range(5):
        bingo(call[r][c])
        if l_dia == 5 and not visited_ldia:
            visited_ldia = 1
            cnt += 1
        if r_dia == 5 and not visited_rdia:
            visited_rdia = 1
            cnt += 1
        for i in range(5):
            if row[i] == 5 and visited_r[i] != 1:
                visited_r[i] = 1
                cnt += 1
            if col[i] == 5 and visited_c[i] != 1:
                visited_c[i] = 1
                cnt += 1

        if cnt >= 3:
            result = 5 * r + (c + 1)
            break
    if cnt >= 3:
        break

print(result)