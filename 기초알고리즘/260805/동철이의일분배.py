# 직원 N명, 할 일 N개 -> 확률의 최댓값 구하기
def work(idx, sm):
    global max_prob
    # 가지치기: 확률이 이미 최댓값보다 작다면 앞으로 곱해도 작아지기만 하니까
    if sm < max_prob:
        return
    # 종료조건: N번째 직원까지 모두 할당
    if idx == N:
        if max_prob < sm:
            max_prob = sm
        return
    # 일 주기
    for k in range(N):
        if v[k] == 0 and arr[idx][k] != 0:
            v[k] = 1
            work(idx+1, sm * (arr[idx][k] / 100))
            v[k] = 0

for T in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*N

    max_prob = 0
    work(0, 1)
    print(f'#{T} {max_prob * 100:.6f}')