# 1번 start, 바이러스 양방향
# 컴퓨터 수는 100 이하

# dfs 정의
def dfs(cur):
    # 첫 방문 & 방문 표시
    visit[cur] = 1

    # 동작
    for nxt in adj[cur]:
        if visit[nxt] == 0:
            dfs(nxt)

# 입력 받기
computer = int(input())
link = int(input())
adj = [[] for _ in range(computer+1)]
for _ in range(link):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

# 필요한 리스트 설정
visit = [0] * (computer+1)

# 결과 출력
dfs(1)

sum = 0
for i in range(computer + 1):
    if visit[i] == 1:
        sum += 1
print(sum-1)
