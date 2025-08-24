# 25.08.24

while True:
    tc = input()
    if tc == '0':
        break

    reverse = tc[-1::-1]
    if tc == reverse:
        print('yes')
    else:
        print('no')
