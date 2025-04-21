# 25.04.21

def bingo(check):
    flag = False
    for i in range(5):
        for j in range(5):
            if board[i][j] == check:
                row[i] += 1
                col[j] += 1
                if i == j:
                    l_dia[i] += 1
                if j == 4 - i:
                    r_dia[i] += 1
                flag = True
                break
        if flag:
            break


board = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]

row = [0] * 5
col = [0] * 5
l_dia = [0] * 5
r_dia = [0] * 5

cnt = 0
result = 0
for r in range(5):
    for c in range(5):
        bingo(call[r][c])
        if 5 in row or 5 in col or 0 not in l_dia or 0 not in r_dia:
            cnt += 1
            if cnt == 3:
                result = 5 * r + (c + 1)
                break

print(result)