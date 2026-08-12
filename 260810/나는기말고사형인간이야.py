# 한시간당 올릴 수 있는 점수가 높은 순으로 시간을 채워가면 될듯

N, M = map(int, input().split())    # N 남은 일수 / M 과목수
alst = list(map(int, input().split()))  # 공부 안해도 받는 최저점
blst = list(map(int, input().split()))  # 1시간당 올릴 수 있는 점수

# 큰 점수 순으로 정렬하기. 같은 점수면 최저점 낮은 과목부터.
lst = [[0,0] for _ in range(M)]
for i in range(M):
    lst[i][0], lst[i][1] = alst[i], blst[i]
lst.sort(key = lambda x: (-x[1], x[0]))

idx = 0
score = lst[0][0]
tot_score = score

# 효율이 제일 좋은 과목의 최소 점수
for time in range(24*N+1):

    # 1시간 공부했을 때 100을 넘지 않으면 그냥 공부
    if score + lst[idx][1] <= 100:
        score += lst[idx][1]
        tot_score += lst[idx][1]
    else:
        # 남은 과목이 있으면: 남은 점수와 다른 점수 중 더 좋은 것 고르기
        if idx + 1 < len(lst) - 1:
            res = min(100-score, lst[idx+1][0])
            tot_score += res
            idx += 1
            score = lst[idx][0]
            tot_score += score

        # 남은 과목이 없으면: 남은 점수 그냥 채우고 끝
        else:
            tot_score += 100-score
            break

# 시간 내 공부 못한 과목이 있다면
if idx < len(lst)-1:
    tot_score += sum(lst[idx+1:][0])

print(tot_score)
