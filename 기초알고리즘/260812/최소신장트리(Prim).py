for TC in range(1, int(input())+1):

    # 노드번호 V, 간선 개수 E
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]    # 노드번호 0번부터 시작
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append((w, e))
        adj[e].append((w, s))
    visit = [0]*(V+1)   # 노드 방문 표시

    import heapq
    def prim(start, weight):
        hq = []
        cost = 0
        heapq.heappush(hq, (weight, start))

        while hq:
            # 가장 가중치가 낮은 노드를 불러온다
            cur_weight, cur_node = heapq.heappop(hq)

            # 이미 포함된 노드면 X
            if visit[cur_node] == 1:
                continue

            # 아니면 간선 선택
            visit[cur_node] = 1
            cost += cur_weight

            # 현재 노드에서 갈 수 있는 연결된 노드들 넣기
            for nxt_weight, ni in adj[cur_node]:
                if visit[ni] == 0:
                    heapq.heappush(hq, (nxt_weight, ni))

        return cost

    a = prim(0,0)
    print(f'#{TC} {a}')