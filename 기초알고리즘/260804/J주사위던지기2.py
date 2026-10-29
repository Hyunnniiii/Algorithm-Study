def jusawii(cnt, sm, lst):
    # 종료 조건: N번 던졌을 때
    if cnt == N:
        if sm == M:     # 합이 M이면 출력
            print(*lst)
        return
    # 주사위 숫자 고르기
    for k in range(1, 7):
        jusawii(cnt+1, sm + k, lst + [k])

N, M = map(int, input().split())
jusawii(0,0,[])
