N = int(input())
nums = [int(input()) for _ in range(N)]

stk = []
for x in nums:
    # 맨 처음에는 숫자 추가
    if not stk:
        stk.append(x)
    # 해당 숫자보다 작거나 같은 막대기 모두 pop
    # pop을 하는 도중 빈 스택이 될 수 있으므로 while stk 넣어줘야 한다
    else:
        while stk and x >= stk[-1]:
            stk.pop()
        stk.append(x)

print(len(stk))