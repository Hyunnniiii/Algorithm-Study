
def comb(n, start, lst):
    global ans, cnt
    # 정지조건: K개 입력했을 때
    if n == K:
        cnt += 1
        if lst == A:
            ans = cnt
        return
    # 숫자 중복 안되게 추가하기
    for x in range(start, N+1):
        comb(n+1, x+1, lst + [x])

N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = None
cnt = 0

comb(0,1,[])
print(ans)