# 25.03.25

while True:
    lengths = list(map(int, input().split()))
    if lengths == [0, 0, 0]:
        break
    else:
        max_v = max(lengths)
        idx = lengths.index(max_v)
        lengths.pop(idx)
        a, b = lengths
        if max_v**2 == a**2 + b**2:
            print('right')
        else:
            print('wrong')