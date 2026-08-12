for TC in range(1, int(input())+1):

    # 노드번호 V, 간선 개수 E
    V, E = map(int, input().split())

    adj = [list(map(int, input().split())) for _ in range(E)]

    # 가중치 기준 정렬
    adj.sort(key=lambda x : x[2])

    # union 함수 정의
    parent = [i for i in range(V+1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        a = find(x)
        b = find(y)
        parent[b] = a

    tot_cost = 0
    # 가장 작은 가중치의 간선 먼저 확인
    for start, end, weight in adj:

        # 두 노드가 이미 같은 집합이면 -> 선택 X
        if find(start) == find(end):
            continue
        # 다른 집합이면 -> 선택, union
        tot_cost += weight
        union(start, end)

    print(f'#{TC} {tot_cost}')