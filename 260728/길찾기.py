# 길이 존재하면 1, 존재하지 않으면 0
# 일방 통행. 출발지 0, 도착지 99

# for T in range(1, 4):
#     T, E = map(int, input().split())
#
#     # adj 배열 생성
#     adj = [[] for _ in range(100)]
#
#     lst = list(map(int, input().split()))
#     for x in range(E * 2-1):
#         adj[lst[x]].append(lst[x+1])
#         x += 2
#
#     # 사전 정의
#     v = [0]*100
#
#     # 재귀 함수
#     def dfs(cur):
#         # 첫 방문 / 방문 표시
#         v[cur] = 1
#
#         # 99를 방문하면 성공
#         if v[99] == 1:
#             return True
#
#         # 연결된 노드 처리
#         for nxt in adj[cur]:
#             if v[nxt] == 0:
#                 # nxt가 99여서 True를 반환하면 성공
#                 if dfs(nxt):
#                     return True
#                 # 아니면 그 다음을 진행
#
#     success = 1 if dfs(0) else 0
#     print(f'#{T} {success}')

# 사실 위의 방법은 이해가 안된다...

# 재귀를 이용한 다른 방법

# 재귀 함수 정의
def dfs(start):
    # 방문 표시
    visit[start] = 1

    for next in adj[start]:
        # 방문하지 않은 곳이면 다시 dfs
        if visit[next] == 0:
            dfs(next)

for _ in range(1, 11):
    T, E = map(int, input().split())

    # adj 배열 생성
    adj = [[] for _ in range(100)]
    lst = list(map(int, input().split()))
    for x in range(E * 2-1):
        adj[lst[x]].append(lst[x+1])
        x += 2
    # 방문 리스트 생성
    visit = [0]*100

    # 함수 실행
    dfs(0)

    print(f'#{T} {visit[99]}')