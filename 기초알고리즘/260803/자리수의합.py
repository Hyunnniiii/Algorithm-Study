ans = 0
def hap(n):
    global ans
    # 종료조건: 자릿수 다 더했을 때
    if n > len(N)-1:
        return 0
    # 한자리씩 더한다
    return N[n] + hap(n+1)

for T in range(1, int(input())+1):
    N = list(map(int, input()))
    print(f'#{T} {hap(0)}')