# 숫자열 2개 입력 받기
# 둘 중 길이가 긴 숫자열 찾기
# 짧은 숫자열을 둘의 차이만큼 0부터 이동,곱을 각각 구한다
# 이동 횟수는 N-M+1 (ex) 3과 6 길이면 3을 6에 대고 0부터 4번 이동
# 최댓값 출력

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 길이가 긴 리스트를 B로 설정, 큰 수를 M으로 설정
    if len(A) >= len(B):
        A, B = B, A
    if N >= M:
        N,M=M,N

    lst=[]
    for j in range(M-N+1):
        i=0
        mult=0
        for k in range(len(A)):
            mult += A[i]*B[j]
            i += 1
            j += 1
        lst.append(mult)
    
    # 더 간결한 표현
    # for i in range(M-N+1):
    #     mult=0
    #     for k in range(N):
    #         mult += A[k]*B[i+k]
    #     lst.append(mult)

    print(f'#{test_case}', max(lst))