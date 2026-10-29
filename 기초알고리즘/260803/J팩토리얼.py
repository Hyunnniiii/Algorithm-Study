
def factorial(n):
    global num

    # 종료 조건
    if n == 1:
        print('1! = 1 ')
        print(num)
        return

    # 단위행동
    if n > 1:
        print(f'{n}! = {n} * {n-1}! ')
        num = num * n
        factorial(n-1)

num = 1
factorial(int(input()))