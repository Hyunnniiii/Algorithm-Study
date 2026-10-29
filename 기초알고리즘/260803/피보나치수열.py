

def fibonacci(n):
    # 첫번째와 두번째는 1 & 종료
    if n==1 or n==2:
        return 1

    # n 이전 2개의 합을 구한다
    return fibonacci(n-2) + fibonacci(n-1)

for T in range(1, int(input())+1):
    N = int(input())
    print(f'#{T} {fibonacci(N)}')

