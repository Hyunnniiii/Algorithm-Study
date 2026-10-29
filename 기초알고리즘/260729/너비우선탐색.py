for T in range(1, int(input())+1):
    V, E = map(int, input().split())

    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)

    q = [1]
    v = [0]*(V+1)
    ans = []

    # 큐에 데이터 있는 동안 반복
    while q:
        node = q.pop(0)
        ans.append(node)

        for nxt in adj[node]:
            # 안 건드린 곳이면 큐에 추가
            if v[nxt] == 0:
                v[nxt] = 1
                q.append(nxt)
    print(f'#{T}', *ans)