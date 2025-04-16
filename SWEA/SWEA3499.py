# 25.04.16

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(input().split())
    shuffle = []

    if N % 2 == 0:
        head = cards[:N//2]
        tail = cards[N//2:]
    else:
        head = cards[:N//2 + 1]
        tail = cards[N//2 + 1:]

    '''
    <<< 카드 덱 이렇게 나눌걸 >>>
    mid = (N + 1) // 2
    head = card[:mid]
    tail = card[mid:]     
    '''

    for i in range(N // 2 + 1):
        if i < len(head):
            shuffle.append(head[i])
        if i < len(tail):
            shuffle.append(tail[i])

    print(f'#{tc}', end=" ")
    print(*shuffle)
