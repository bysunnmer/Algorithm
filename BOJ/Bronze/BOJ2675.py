# 25.03.20

T = int(input())
for tc in range(T):
    R, S = input().split()
    for s in S:
        print(s*int(R), end="")
    print()