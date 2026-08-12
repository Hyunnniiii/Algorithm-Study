N, M = map(int, input().split())
lst = list(map(int, input().split()))

def funfun(nlst):
    # 종료 조건: M개 나열
    if len(nlst) == M:
        print(*nlst)
        return
    # 숫자 고르기
    for k in range(N):
        if lst[k] not in nlst:
            funfun(nlst + [lst[k]])

funfun([])
