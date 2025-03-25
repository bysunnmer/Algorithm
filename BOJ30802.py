# 25.03.25

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())
t_cnt = 0
p_bundle = N // P
p_single = N % P

for size in sizes:
    if size % T == 0:
        t_cnt += size // T
    else:
        t_cnt += size // T + 1

print(t_cnt)
print(p_bundle, end=" ")
print(p_single)