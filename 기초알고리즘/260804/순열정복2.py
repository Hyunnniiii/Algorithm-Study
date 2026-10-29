N, M = map(int, input().split())

def soon(idx, lst):
    # 종료 조건: M개 선택했을 때
    if len(lst) == M:
        print(*lst)
        return

    for k in range(1, N+1):
        if k not in lst:
            soon(idx+1, lst+[k])

soon(0,[])