# 25.03.24

arr = list(map(int, input().split()))
arr_copy = arr[:]

if arr == sorted(arr_copy):
    print('ascending')
elif arr == sorted(arr_copy, reverse=True):
    print('descending')
else:
    print('mixed')