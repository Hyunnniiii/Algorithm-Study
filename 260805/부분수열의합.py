# 조합 풀이
def dfs(n, start, sm):
    global cnt
    # 가지치기: 합이 K를 넘어갈 때
    if sm > K:
        return
    # 종료 조건: 합이 K
    if sm == K:
        cnt += 1
        return
    # 숫자 고르기
    for x in range(start, N):
        dfs(n+1, x+1, sm+A[x])

for T in range(1, int(input())+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = 0
    dfs(0,0,0)
    print(f'#{T} {cnt}')

# ==========
# 부분집합 풀이
def dfs(idx, sm):
    global cnt
    # 가지치기: 합이 K를 넘어갈 때
    if sm > K:
        return
    # 종료 조건: 합이 K
    if idx == N:
        if sm == K:
            cnt += 1
        return
    # 숫자 고르기
    dfs(idx+1, sm + A[idx] )
    dfs(idx+1, sm )

for T in range(1, int(input())+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    cnt = 0
    dfs(0,0)
    print(f'#{T} {cnt}')

# ====
# 비트연산 풀이
# 최소 1개 이상: 1개 ~ N개
