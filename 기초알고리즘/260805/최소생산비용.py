def factory(idx, start, sm):
    global min_cost
    # 가지치기: 이미 최소값 넘어버린 경우
    if sm > min_cost:
        return
    # 종료조건
    if idx == N:
        if min_cost > sm:
            min_cost = sm
        return
    # 선택
    for j in range(0,N):
        if v[j] == 0:
            v[j] = 1
            factory(idx+1, j+1, sm + arr[idx][j] )
            v[j] = 0

for T in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*N
    min_cost = 99*N + 1

    factory(0, 0, 0)
    print(f'#{T} {min_cost}')