N, M = map(int, input().split())    # N 정점, M 간선
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = list(map(int, input().split()))
    adj[s].append(e)
    adj[e].append(s)


visit = [0] * (N+1)
q = []
node = [i for i in range(1,N+1)]

count = 0
while node:
    q.append(node[0])
    visit[node[0]] = 1
    while q:
        a = q.pop(0)
        node.remove(a)

        for nxt in adj[a]:
            if visit[nxt] == 0:
                visit[nxt] = 1
                q.append(nxt)
    count += 1
print(count)
