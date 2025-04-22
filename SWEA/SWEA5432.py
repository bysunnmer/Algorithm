# 25.04.22

# 자신보다 긴 쇠막대기 위에만 놓일 수 있음
# 위에 놓을 땐 완전히 포함되도록 놓되, 끝점은 겹치지 않도록
# 레이저는 하나 이상 존재
# 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않음

T = int(input())
for tc in range(1, T+1):
    assign = list(input())
    stack = []
    lasers = []
    cnt = 0
    '''
    () ( ( ( () () ) ( () ) () ) ) ( () )
       - - -       - -    -    - -
    
    지금 스택 ( ( (
    '''
    for i, a in enumerate(assign):
        if a == '(':
            stack.append((i, a))
            lasers.append(0)
        else:
            if stack and stack[-1][0] == i-1:   # stack 의 top '(' 가 직전 것 일 경우 레이저
                stack.pop()
                lasers.pop()
                if lasers:
                    for laser in lasers:
                        laser += 1
            else:
                stack.pop()
                cnt += (lasers.pop() + 1)

    print(cnt)