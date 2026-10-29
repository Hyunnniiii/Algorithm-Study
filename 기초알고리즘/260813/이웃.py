# N개의 집, N명의 학생, 한 집에는 한명씩 거주
# i번 학생이 사는 집의 좌표는 i -> 인덱스 주의
# 학교는 1번과 2번이 있고, 각 학생은 둘 중 하나의 학교를 다님
# 같은 학교 : 거리 K1 이하 / 다른 학교: 거리 K2 이하
# 자기 자신은 자신의 이웃이 아니다
N, K1, K2 = map(int, input().split())
lst = [0] + list(map(int, input().split()))     # 인덱스 맞추려고 앞에 0 더함 주의
neighbor = [0]*(N+1)

# 앞에서부터 차례로 비교하면서 이웃인 애들 동시에 +1
for idx in range(1, N):   # 나
    for nxt in range(idx+1, N+1):      # 비교할 사람

        # 학교가 같을 때
        if lst[idx] == lst[nxt]:
            if abs(idx - nxt) <= K1:
                neighbor[idx] += 1
                neighbor[nxt] += 1
        # 학교가 다를 때
        if lst[idx] != lst[nxt]:
            if abs(idx - nxt) <= K2:
                neighbor[idx] += 1
                neighbor[nxt] += 1
print(*neighbor[1:])