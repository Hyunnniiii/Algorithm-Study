def T1(cnt, lst):
    if cnt == N:    # N번 던지면 종료
        print(*lst)
        return
    for k in range(1,7):    # 중복 허용해서 모든 경우 출력
        T1(cnt+1, lst + [k])

def T2(cnt, start, lst):
    if cnt == N:    # N번 던지면 종료
        print(*lst)
        return
    for k in range(start,7):    # 중복 제외하고 출력
        T2(cnt+1, k, lst + [k])

def T3(cnt, lst):
    if cnt == N:    # N번 던지면 종료
        print(*lst)
        return
    for k in range(1, 7):    # 모두 다른 수가 되게 출력
        if k not in lst:
            T3(cnt+1, lst + [k])

N, type = map(int, input().split())
if type == 1:
    T1(0, [])
elif type == 2:
    T2(0, 1, [])
elif type == 3:
    T3(0, [])