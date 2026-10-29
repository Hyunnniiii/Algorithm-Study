def seq(n):
    # 종료조건: N번째 넘어갈 때
    if n > N:
        return

    # 첫 번째 수는 1
    if n == 1:
        return 1

    # 2개 수의 합 리턴
    return seq(n-1) + seq(n//2)

for T in range(1, int(input())+1):
    N = int(input())
    print(f'#{T} {seq(N)}')