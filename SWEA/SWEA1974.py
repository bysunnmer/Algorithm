# 25.04.15

T = int(input())
for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    flag = True

    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            lst = []
            for i in range(3):
                lst += puzzle[r+i][c:c+3]
            if len(set(lst)) != 9:
                flag = False
                break


    for row in puzzle:
        if len(set(row)) != 9:
            flag = False
            break

    for c in range(9):
        col = []
        for r in range(9):
            col.append(puzzle[r][c])
        if len(set(col)) != 9:
            flag = False
            break

    if flag:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')