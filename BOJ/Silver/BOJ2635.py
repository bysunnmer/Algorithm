# 25.04.21

lst = []
first = int(input())
lst.append(first)
max_len = 0
max_lst = []

for second in range(first+1):
    lst.append(second)
    next_num = lst[-2]-lst[-1]
    while next_num >= 0:
        lst.append(next_num)
        next_num = lst[-2]-lst[-1]

    max_len = max(max_len, len(lst))
    if max_len == len(lst):
        max_lst = lst
    lst = [first]

print(max_len)
print(*max_lst)