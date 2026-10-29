N = int(input())
dp = [0]*(N+1)
dp[1] = 1

def fibo(n):
    # 종료조건: 0까지 왔을 때
    if n == 0:
        return 0

    # dp에 저장한 값을 가져온다 -> 중복 계산 방지
    if dp[n] != 0:
        return dp[n]

    # 피보나치 수열 점화식
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

print(fibo(N))