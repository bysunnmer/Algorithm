# 25.03.13 / 25.03.15

T = int(input())

for tc in range(1, T+1):
  n = int(input())
  have = []
  kind = []
  cnt = 1

  for _ in range(n):
    c, k = input().split()
    have.append([c, k])
    kind.append(k)

    copy_kind = kind
    copy_kind = list(set(copy_kind))

  for ck in copy_kind:
    cnt *= kind.count(ck) + 1

  print(cnt - 1)

'''
조합으로 시도했을 때도 의상 종류마다 의상 개수 세는 방법이 안 떠올라서 못 풀었는데
굳이 조합이 아니어도 식을 도출해서 풀이할 수 있는 방법을 배웠다.

한 의상 종류마다 입을 수 있는 가짓 수 = (의상 개수 + 안 입는 경우 1)
위의 가짓 수와 의상 종류의 수를 곱한 총 경우의 수에서 모든 종류를 안 입을 때의 경우인 1을 빼주는 식 도출 가능

의상의 개수를 세는 방법은 위의 방식처럼 의상 종류에 대한 리스트를 복사하고
해당 리스트를 튜플로 중복제거 한 뒤 다시 리스트 처리를 해서 for 문을 돌며 원본과 복사본을 비교하는 방식이 있고


dict1 = {}

key = input()
if not dict1.get(key):    <<< dict1에 없으면 none 반환
  dict1[key] = 1
else:
  dict1[key] += 1
  
이렇게 개수를 셀 수도 있음


+++) gpt가 알려준 set과 dict 활용한 방법
original = [1, 2, 2, 3, 3, 3, 4, 5]
unique_list = list(set(original))  # 중복 제거 후 리스트로 변환

count_dict = {num: original.count(num) for num in unique_list}  # 각 숫자의 개수 세기
print(count_dict)  # {1: 1, 2: 2, 3: 3, 4: 1, 5: 1}

'''