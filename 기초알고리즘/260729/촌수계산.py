n = int(input())    # 사람 수
start, end = map(int, input().split())
m = int(input())    # 관계 수

adj = [[] for _ in range(n+1)]    # 가족 관계 입력
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

q = [start]      # 사람 큐
chon = [0]*(n+1)   # 촌수
answer = 0

while q:
    cur = q.pop(0)

    for nxt in adj[cur]:
        # 안 본 사람이면 큐에 추가, 촌수 +1
        if chon[nxt] == 0 and nxt != end:
            q.append(nxt)
            chon[nxt] = chon[cur] + 1
        # 정답이면 큐 초기화, 촌수 계산
        elif chon[nxt] == 0 and nxt == end:
            answer = chon[cur] + 1
            q = []
            break
# 경로가 없으면 -1 출력
if answer == 0:
    answer = -1
print(answer)

# ====================
# 위의 코드는 첫 번째 노드를 0으로 잡아서
# 다른 노드에서 시작점을 또 큐에 넣을 수 있다

n = int(input())    # 사람 수
start, end = map(int, input().split())
m = int(input())    # 관계 수

adj = [[] for _ in range(n+1)]    # 가족 관계 입력
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

q = [start]      # 사람 큐

# 맨 처음 배열을 -1로 통일하고, 시작점을 0으로 설정
chon = [-1]*(n+1)   # 촌수
chon[start] = 0

while q:
    cur = q.pop(0)

    for nxt in adj[cur]:
        # 방문 안한 곳이면 > 거리 수정, 큐에 추가
        if chon[nxt] == -1:
            chon[nxt] = chon[cur] + 1
            q.append(nxt)

# 도착점의 거리가 몇인지 바로 출력
print(chon[end])
