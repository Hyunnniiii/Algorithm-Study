# 집에서 가장 가까운 대피소로 이동
# 그 중 가장 긴 거리가 최소가 되도록 대피소를 설치

N, K = map(int, input().split())
home = [list(map(int, input().split())) for _ in range(N)]

# 대피소를 K개 선택하고
# 각 집마다 거리를 구해서 그거의 최댓값을 구했을 때
# 그 최댓값이 가장 최소인 대피소 조합을 선택, 그때의 최댓값 구하기

# 집이 N개 있으니까 그 중 2개 고르는 조합을 인덱스로
hlst = []
def choose(idx, lst, cnt):
    global hlst
    # 조기종료: 2개 골랐을 때
    if cnt == K:
        hlst += [lst]
        return
    # 종료: N개에 대한 선택 마쳤을 때
    if idx == N:
        return
    # 고르기
    choose(idx+1, lst + [idx], cnt + 1)
    choose(idx+1, lst, cnt)

choose(0, [], 0)

ans = float('inf')
# idx: hlst의 몇 번째 조합까지 돌았는지
def depi(idx):
    global ans

    # 종료: hlst의 모든 조합 다 돌았을 때
    if idx == len(hlst):
        return

    # 각 집마다의 거리 구하기
    shelter = hlst[idx]

    # 각 집마다 가까운 대피소 선택
    lst = []
    for k in range(N):
        min_dist = float('inf')

        for s in shelter:
            # 각 집마다 가까운 대피소의 거리: dist
            d = abs(home[s][0] - home[k][0])+abs(home[s][1] - home[k][1])
            min_dist = min(d, min_dist)
        lst.append(min_dist)

    # 한 조합당 가까운 대피소의 거리 중 가장 먼 대피소의 거리: far
    far = max(lst)

    # 최대 중 최소만 남기기
    ans = min(ans, far)

    depi(idx+1)

depi(0)
print(ans)


# ==================
N, K = map(int, input().split())
home = [list(map(int, input().split())) for _ in range(N)]

ans = float('inf')

def choose(idx, shelter):
    global ans

    # 대피소 K개 선택 완료
    if len(shelter) == K:

        # 각 집의 가장 가까운 대피소 거리를 저장
        lst = []

        for h in range(N):
            min_dist = float('inf')

            # 현재 집 h에서 K개 대피소까지 거리 확인
            for s in shelter:
                d = abs(home[s][0] - home[h][0]) + \
                    abs(home[s][1] - home[h][1])

                min_dist = min(min_dist, d)

            lst.append(min_dist)

        # 이 대피소 조합에서 가장 먼 집
        far = max(lst)

        # 조합별 far 중 최소
        ans = min(ans, far)

        return

    # 모든 집에 대한 선택이 끝났을 때
    if idx == N:
        return

    # idx번째 집을 대피소로 선택
    choose(idx + 1, shelter + [idx])

    # idx번째 집을 대피소로 선택하지 않음
    choose(idx + 1, shelter)


choose(0, [])

print(ans)