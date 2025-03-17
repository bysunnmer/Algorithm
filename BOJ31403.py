# 25.03.17

A = input()
B = input()
C = input()

number = [A, B, C]
number = list(map(int, number))
num_res = number[0] + number[1] - number[2]
char = int(A + B)
char_res = char - number[2]

print(num_res)
print(char_res)


'''
<<최적화>>
a = input()
b = input()
c = input()
print(int(a) + int(b) + int(c))
print(int(a + b) - int(c))
'''