# 25.03.12
import sys
N = int(input())
stack = []
for _ in range(N):
  o = list(sys.stdin.readline().split())    # 속도를 위해서

  if o[0] == "1":
    stack.append(int(o[-1]))
  elif o[0] == "2":
    if stack:
      print(stack.pop())
    else:
      print(-1)
  elif o[0] == "3":
    print(len(stack))
  elif o[0] == "4":
    if stack == []:
      print(1)
    else:
      print(0)
  else:
    if stack:
      print(stack[-1])
    else:
      print(-1)
