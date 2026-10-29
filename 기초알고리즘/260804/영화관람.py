# 소들의 무게의 합이 C를 넘지 않는 최댓값 구하기

def movie(start, sm):
    global min_gap
    # C를 넘으면 가지치기
    if C < sm:
        return

    # C를 안 넘을 때까지 차이를 구하기
    if C - sm < min_gap:
        min_gap = C - sm

    # 소 추가
    for k in range(start, N):
        movie(k+1, sm + cow[k])


C, N = map(int, input().split())
cow = list(int(input()) for _ in range(N))
min_gap = C

movie(0,0)
print(C - min_gap)