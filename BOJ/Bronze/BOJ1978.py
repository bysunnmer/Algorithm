# 25.04.05 / 25.06.13
import math

N = int(input())
nums = list(map(int, input().split()))
result = 0

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

for n in nums:
    if is_prime(n):
        result += 1

print(result)
