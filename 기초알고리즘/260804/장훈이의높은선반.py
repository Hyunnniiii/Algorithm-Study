# 선반 높이 B / 점원 수 N / 각 점원의 키 Hi
# 높이가 B 이상인 탑 중에서 가장 낮은 탑의 높이

def tower(idx, sm):
    global S
    # 종료 조건: B보다 커졌을 때
    if sm >= B:
        if sm < S:
            S = sm
        return
    # 점원 고르기: 중복 X
    for k in range(idx, N):
        tower(k + 1, sm + height[k])

for T in range(1, int(input())+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    S = sum(height) # 기준으로 min값 구하면 될듯

    tower(0,0)
    print(f'#{T} {S-B}')
