def dice(n, lst):
    # 종료 조건: N번 던졌을 때
    if n == N:
        print(*lst)
        return

    # 하부 함수
    for k in range(1, 7):
        if n ==0:
            dice(n+1, lst + [k])
        elif lst[-1] <= k:
            dice(n+1, lst + [k])

for T in range(1, int(input())+1):
    N = int(input())
    print(f'#{T}')
    dice(0, [])


# ==========
# n: 던진 횟수 -> 트리 표현 -> 코드
 def dfs(n, start, alst):
    if n == N:
        print(*alst)
        return
    for j in range(start, 7):
        dfs(n+1, j, alst + [j])
