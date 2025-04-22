# 25.04.22

# 자신보다 긴 쇠막대기 위에만 놓일 수 있음
# 위에 놓을 땐 완전히 포함되도록 놓되, 끝점은 겹치지 않도록
# 레이저는 하나 이상 존재
# 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않음


'''
() ( ( ( () () ) ( () ) () ) ) ( () )
   - - -       - -    -    - -

지금 스택 ( ( (
'''


T = int(input())
for tc in range(1, T+1):
    assign = list(input())
    stack = []
    lasers = []
    cnt = 0
    for i, a in enumerate(assign):
        if a == '(':
            stack.append((i, a))
            lasers.append(0)
        else:
            if stack and stack[-1][0] == i-1:   # stack 의 top '(' 가 직전 것 일 경우 레이저
                stack.pop()
                lasers.pop()
                if lasers:
                    for idx in range(len(lasers)):     # for laser in lasers 로 하려고 했는데
                        lasers[idx] += 1               # 이때 laser 는 리스트 내의 해당 값을 복사해서 받는 지역변수라
            else:                                      # 원본 리스트 안의 요소가 바뀌지 않음
                stack.pop()
                cnt += (lasers.pop() + 1)

    print(f'#{tc} {cnt}')


