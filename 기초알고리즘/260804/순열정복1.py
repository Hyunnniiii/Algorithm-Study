N, M = map(int, input().split())
lst = []

def soon(n, lst):
    # 종료 조건: M개 선택했을 때
    if len(lst) == M:
        print(*lst)
        return

    # 그 다음 수 선택
    for j in range(1, N+1):
        soon(n+1, lst + [j])

soon(0, [])

