N = int(input())    # 동전 단위 개수
coin = [0] + list(map(int, input().split()))      # 동전 단위
W = int(input())    # 잔돈

# 최종 금액에서 내가 가진 동전 금액별로 빼가면서 dp를 해보자
# False는 숫자계산에서 0으로 취급되므로 절대 기본값으로 두면 안됨 주의
dp = [float('inf')]*(W+1)
for k in coin:
    dp[k] = 1
dp[0] = 0

for x in range(1, W+1):
    clst = []   # 횟수 저장
    for c in coin[1:]:
        if dp[x] == float('inf') and x-c >= 0:
            a = dp[x-c] + 1
            clst.append(a)
    if clst:
        dp[x] = min(clst)

if dp[W] != float('inf'):
    print(dp[W])
else:
    print('impossible')