T = int(input())

def comb(cnt, start):
  if cnt == 1:
    kind.append(*path)

  for idx in range(start, len(lst)):
    path.append(lst[idx])
    comb(cnt + 1, idx + 1)
    path.pop()

for tc in range(1, T+1):
  have = []
  lst = []
  path = []
  kind = []
  n = int(input())
  for _ in range(n):
    c, k = input().split()
    have.append([c, k])

  
  # for in range(n): have[1] 을 빈 리스트에 없는 경우 append (또는 set)
  for h in have:
    if h[1] not in lst:
      lst.append(h[1])
  print(lst)
  comb(0, 0)
  print(kind)
  cnt = 0
  for i in range()