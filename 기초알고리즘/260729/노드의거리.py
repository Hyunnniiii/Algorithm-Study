for T in range(1, int(input())+1):
    V, E = map(int, input().split())

    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        adj[start].append(end)
        adj[end].append(start)

    S, G = map(int, input().split())

    # 주어진 출발 노드에서 최소 몇 개의 간선을 지나면
    # 도착 노드에 갈 수 있는지 알아내는 프로그램
    # 못가면 0을 출력

    # 초기 세팅
    visit = [0]*(V+1)   # 방문하면 표시
    visit[S] = 1
    q = [S]     # 갈 곳들
    route = [0]*(V+1)   # 경로의 길이

    while q:
        node = q.pop(0)

        for nxt in adj[node]:
            if visit[nxt] == 0:
                q.append(nxt)
                visit[nxt] = 1
                route[nxt] = route[node] + 1
    print(f'#{T}', route[G])
