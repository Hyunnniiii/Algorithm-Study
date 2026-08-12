for T in range(1, int(input())+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]

    # adj 생성
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)

    # stk: 스택, v: 방문한 노드에 1 표시, and: 방문한 노드 기록
    stk = []
    v = [0]*(V+1)
    ans = []

    # 확인할 노드 받기
    S, G = map(int, input().split())

    # 첫 방문
    cur = S
    v[cur] = 1
    ans.append(S)

    # 찾으려는 노드가 나오면 성공, 아니면 실패
    success = 0
    while True:
        for nxt in adj[cur]:
            if v[nxt] == 0:
                if nxt == G:
                    success = 1
                else:
                    stk.append(cur)
                    cur = nxt
                    ans.append(cur)
                    v[cur] = 1
                    break
        else:
            if stk:
                cur = stk.pop()
            else:
                break
    print(f'#{T} {success}')
