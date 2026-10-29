for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    smm = []
    for i in range(N-M+1):
        tot = 0
        for j in range(M):
            tot += lst[i+j]
        smm.append(tot)
    print(f'#{test_case}', max(smm)-min(smm))
