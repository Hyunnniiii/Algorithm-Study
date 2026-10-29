N = int(input())    # 학생 수
M = int(input())    # 관계 수

# 친구 관계 리스트 생성
friend = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, list(input().split()))
    friend[start].append(end)
    friend[end].append(start)

# 1번에서 시작해서 거리가 2 이하인 사람의 수를 구한다
q = [1]
visit = [0]*(N+1)
visit[1] = 1
dist = [0]*(N+1)    # 0번 인덱스 거리 주의

# 시작
while q:
    a = q.pop(0)

    for nxt in friend[a]:
        if visit[nxt] == 0:
            q.append(nxt)
            visit[nxt] = 1
            dist[nxt] = dist[a] + 1
count = 0
for x in dist:
    if 0 < x <= 2:
        count += 1
print(count)