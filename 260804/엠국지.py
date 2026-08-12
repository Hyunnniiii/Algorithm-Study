def Mgookgi(n, start, lst):
    global cnt
    # 종료 조건: M번 더했을 때 합이 k면 카운트 +1
    if n == M:
        if sum(lst) == K:
            cnt += 1
        return cnt
    # 하부 함수: 이전에 더한 국가 제외, 서로 다른 3개 국가의 국력 더한다
    for j in range(start, N):
       Mgookgi(n+1, j+1, lst + [V[j]])

for T in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    V = list(map(int, input().split()))
    cnt = 0

    print(f'#{T}', end = ' ')
    Mgookgi(0, 0, [])
    print(cnt)

# =========================
