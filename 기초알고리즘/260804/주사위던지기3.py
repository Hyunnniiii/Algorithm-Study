def dice(n, lst):
    # 종료조건: 주사위 N번 던지면 끝
    if n == N:
        if sum(lst) == M:
            print(*lst)
        return

    # 하부 함수
    for k in range(1,7):
        dice(n+1, lst + [k])

for T in range(1, int(input())+1):
    N, M = map(int, input().split())
    print(f'#{T}')
    dice(0, [])
