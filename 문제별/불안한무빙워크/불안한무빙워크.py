# 14:36 시작
# 14:56 구상완료
# 15:01 사람들을 큐로 관리하면 될 것 같다. 어차피 올라간 순서대로 n에 도달하지 않을까? 라는 생각
# 15:17 1차 코딩 완 but while문이 무한 반복된다
# 15:40 일단 꾸역꾸역 됨.. 제출해봄 > fail
# 16:07 중단
# 밥먹고 옴
# 19:05 다시 시작했다가 중단 꽈배기 먹기 시작
# 19:16 다시 시작
# 20:14 중단

from collections import deque

# [0] 입력받기
n, k = map(int, input().split())
rail = list(map(int, input().split()))

# [1] 필요한 자료 생성
rail_idx = 0    # 항상 시작점을 가리킬 포인터
Q = deque()    # 올라간 사람 저장할 큐 (올라간 순서, 현재 idx)
people = [0] * (2*n)  # 사람 유무 저장할 큐

## 시작
ans = 0
stable = True
while stable:
    # 1. 무빙워크 회전하기
    rail_idx = (rail_idx - 1) % (2*n)       # 1번칸의 위치 idx
    n_idx = (rail_idx + n-1) % (2*n)    # 회전했을 때 기준 n번째 위치의 idx

    # n번째에 사람이 있으면 > 즉시 내린다
    if people[n_idx] != 0:
        Q.popleft()
        people[n_idx] = 0

    # 2. 올라간 사람들 이동하기
    cnt = []
    if Q:
        for p in Q:
            nxt = (p+1) % (2*n)
            # 이 사람의 앞 칸에 사람이 없고, 안정성이 0보다 크면 이동.
            # 이동하면 그 칸의 안정성 -1
            if rail[nxt] > 0 and people[nxt] == 0:
                cnt.append(p)
                people[p] = 0
                rail[nxt] -= 1
                people[nxt] = 1

    # 이동할 때 큐에 들어간 사람의 좌표도 같이 nxt로 바뀌어야 한다
    for i in cnt:
        find_idx = Q.index(i)
        Q[find_idx] = (Q[find_idx]+1) % (2*n)

    # n번째에 사람이 있으면 > 즉시 내린다
    if people[n_idx] == 1:
        Q.popleft()
        people[n_idx] = 0

    # 3. 1번 칸 확인하기
    # 안정성이 0이 아니고 사람도 없으면 > 사람 올리고, 안정성 -1
    if rail[rail_idx] != 0 and people[rail_idx] == 0:
        Q.append(rail_idx)
        people[rail_idx] = 1
        rail[rail_idx] -= 1

    # n번째에 사람이 있으면 > 즉시 내린다
    if people[n_idx] == 1:
        Q.popleft()
        people[n_idx] = 0

    # 4. 안정성 0인 곳의 개수 확인
    check = 0
    for s in rail:
        if s == 0:
            check += 1

            if check >= k:
                stable = False
                break

    # 위의 과정 완료하면 테스트 횟수 +1
    ans += 1

print(ans)