# # 물건을 모두 배달하고 회사로 돌아오기 위한 최소의 비용
# # 배달해야 하는 장소는 1번씩만 방문. 배달하고 다시 회사로 돌아온다.
# # 방향에 따라 가격이 다름. 비용 0인 곳은 못 감
# # 1번에서 출발, 마지막에 1번으로 돌아와야 함
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# visit = [[0]*N for _ in range(N)]
# min_cost = 100*N + 1
#
# def delivery(n, start, cost):
#     global visit, min_cost
#     # # 가지치기: 이미 최소비용 넘어가면 종료
#     # if cost > min_cost:
#     #     return
#
#     # 종료 조건: 모두 갔을 때. 마지막으로 1번으로 복귀
#     if n == N-1:
#         cost += arr[start][0]
#         min_cost = min(cost, min_cost)
#         return
#
#     # 배달
#     cnt = 0
#     for k in range(1, N):
#         if visit[start][k] == 0 and arr[start][k] != 0:
#             visit[start][k], visit[k][start] = 1, 1
#             delivery(n+1, k ,cost + arr[start][k])
#             visit[start][k], visit[k][start] = 0, 0
#
#     #     # 갈 곳이 없는 경우 세기
#     #     if visit[start][k] == 1 or arr[start][k] == 0:
#     #         cnt += 1
#     # if cnt == N-1:
#     #     min_cost = 0
#     #     return
#
# delivery(0,0,0)
# print(min_cost)


# 물건을 모두 배달하고 회사로 돌아오기 위한 최소의 비용
# 배달해야 하는 장소는 1번씩만 방문. 배달하고 다시 회사로 돌아온다.
# 방향에 따라 가격이 다름. 비용 0인 곳은 못 감
# 1번에서 출발, 마지막에 1번으로 돌아와야 함

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visit = [0]*N
min_cost = 100*N + 1

def delivery(n, start, cost):
    global visit, min_cost
    # 가지치기: 이미 min값 이상이면 종료
    if cost > min_cost:
        return

    # 종료 조건: (N-1)군데 모두 갔을 때. 마지막으로 1번으로 복귀
    if n == N-1:
        if arr[start][0] == 0:
            return

        cost += arr[start][0]
        min_cost = min(cost, min_cost)
        return
    # 배달
    for k in range(1, N):
        if visit[k] == 0 and arr[start][k] != 0:
            visit[k] = 1
            delivery(n+1, k ,cost + arr[start][k])
            visit[k] = 0

delivery(0,0,0)
if min_cost == 100*N + 1:
    print(0)
else:
    print(min_cost)

# =================================================================
# 조합?? 근데 선택 하고 말고가 되나?