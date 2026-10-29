# 3 <= N <= 10 / -300 <= M <= 300 / -100 <= V <= 100
for T in range(1, int(input())+1):
    # N: 나라 수 / M: 찾을 국력의 합
    N, M = map(int, input().split())

    # v: N개 나라의 국력 리스트
    v = list(map(int, input().split()))

    # 임의의 3개 나라의 국력의 합이 특정 값이 되는 경우가 몇 가지인지
    # 123 124 125 ... 234 235 236 ... 이런식으로
    cnt = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1, N):
                v_sum = v[i] + v[j] + v[k]

                if v_sum == M:
                    cnt += 1
    print(f'#{T} {cnt}')