N, M = map(int, input().split())
lst = []

def soon(start, lst):
    # 종료조건: M개 선택했을 때
    if len(lst) == M:
        print(*lst)
        return

    # 숫자 선택
    for k in range(start, N+1):
        soon(k, lst + [k])

soon(1, [])