N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    adj[start].append((end, cost))
D = [float('inf')]*(N+1)

from heapq import heappush, heapify, heappop

def route(s_cost, si):
    q = []
    heappush(q, (s_cost, si))

    while q:
        now, ci = heappop(q)

        # 현재 저장된 거리가 더 짧으면 갱신
        if D[ci] < now:
            continue
        D[ci] = now

        # 연결된 노드 탐색
        for ni, next_d in adj[ci]:
            if now + next_d < D[ni]:
                heappush(q, (now + next_d, ni))

route(0, 1)
print(D[N])