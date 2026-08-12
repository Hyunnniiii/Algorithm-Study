N = int(input())
lst = list(input().split())

ops = ['*', '/', '+', '-']
stk = []

for x in lst:
    # 연산자가 나오기 전까지 숫자 추가
    if x not in ops:
        stk.append(int(x))

    # 연산자가 나왔을 때
    else:
        b = int(stk.pop())    # 뒤쪽 숫자
        a = int(stk.pop())   # 앞쪽 숫자
        # 연산 정의
        if x == '*':
            stk.append(a * b)
        elif x == '/':
            stk.append(int(a // b))
        elif x == '+':
            stk.append(int(a + b))
        elif x == '-':
            stk.append(int(a - b))
print(stk)