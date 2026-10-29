# 만약에 굴리다가 0 되면 어캄 > 그냥 아쉬운거..
# 구간 길이가 1일 때 / 시간이 1일 때 주의해서 보기
# 뚱이에게 후진은 없다

# 맨 끝 지점에서 차기를 하면 범위 넘어가버리는디
# M초 내에 가장 크게 >> M초 이전에 가장 커도 된다는 것인가

# 백트래킹이다
for TC in range(1, int(input())+1):
    # 직선 구간 길이 N / 굴리는 제한 시간 M
    N, M = map(int, input().split())

    road = [0] + list(map(int, input().split()))

    score = 1
    max_score = -1
    def ddong(idx, time):       # idx: 현재 위치 / time: 소요한 시간
        global score, max_score

        max_score = max(max_score, score)
        # 종료: 직선 길이(N) 초과
        if idx > N:
            return
        # 종료: 제한시간(M)까지 모두 굴렸을 때
        if time == M:
            return

        # 굴리기
        if idx + 1 <= N:    # 밀기
            score += road[idx+1]
            ddong(idx+1, time+1)
            score -= road[idx+1]

        if idx + 2 <= N:    # 차기
            remember = score
            score = (score//2) + road[idx+2]
            ddong(idx+2, time+1)
            score = remember

    ddong(0,0)
    print(f'#{TC} {max_score}')