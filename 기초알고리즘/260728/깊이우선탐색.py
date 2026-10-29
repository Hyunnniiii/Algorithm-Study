# for T in range(1, int(input()) + 1):
#     V, E = map(int, input().split())    # V는 정점 E는 간선
#
#     # adj 입력받기
#     adj = [[] for _ in range(V+1)]
#
#     for _ in range(E):
#         s, e = map(int, input().split())
#         adj[s].append(e)
#         adj[e].append(s)
#
#     # 조건: 낮은 번호의 정점을 우선적으로 방문
#     for row in adj:
#         row.sort()
#     print(adj)
#
#     # v, stk, ans 정의
#     v = [0] * (V+1)
#     stk = []
#     ans = []
#
#     # 시작 위치 표시
#     cur = 1
#     ans.append(cur)
#     v[cur] = 1
#
#     # 루프 시작
#     while True:
#         # cur에 연결된 노드를 하나씩 탐색한다
#         for nxt in adj[cur]:
#             if v[nxt] == 0:
#                 stk.append(cur)
#                 cur = nxt
#                 ans.append(cur)
#                 v[cur] = 1
#                 break
#         # 종점에 도달했을 때
#         else:
#             # stk에 남아있을 때
#             if stk:
#                 cur = stk.pop()
#             # stk에 아무것도 없을 때 -> 끝
#             else:
#                 break
#     print(f'#{T}', *ans)


# ===============

for T in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]

    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)

    for row in adj:
        row.sort()

    v = [0] * (V+1)
    ans = []
    stk = []

    # 첫 방문
    cur = 1
    ans.append(1)
    stk.append(1)
    v[cur] = 1

    # 이후 루프
    while True:
        for nxt in adj[cur]:
            # 방문하지 않은 곳이 있을 때 -> 업데이트
            if v[nxt] == 0:
                stk.append(cur)
                cur = nxt

                v[cur] = 1
                ans.append(cur)
                break
        # 모두 방문했을 때
        else:
            # stk에 남아있을 때 -> 돌아가기
            if stk:
                cur = stk.pop()
            # stk에 아무것도 없을 때 -> 끝
            else:
                break

    print(f'#{T}', *ans)

