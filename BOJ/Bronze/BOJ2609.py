# 25.08.24

nums = list(map(int, input().split()))
nums.sort()

big = nums[1]
small = nums[0]
check = big % small
    
while check != 0:
    big = small
    small = check
    check = big % small

max_div = small

min_mul = int(nums[0] * nums[1] / max_div)

print(max_div)
print(min_mul)
