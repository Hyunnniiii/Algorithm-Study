
def bubun(n, start, sm):
    global cnt
    # 종료조건
    if n == N:
        if sm == K:
            cnt += 1
        return
    # 부분집합 찾기
    for k in range(start, 13):
        bubun(n+1, k+1, sm+k)

for T in range(1, int(input())+1):
    N, K = map(int, input().split())    # N: 부분집합 원소의 수, K: 부분 집합의 합
    cnt = 0

    bubun(0, 1, 0)
    print(f'#{T} {cnt}')
