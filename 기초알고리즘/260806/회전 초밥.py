# # N 접시 수 / d 초밥 가짓수 / k 연속 접시 수 / c 쿠폰 번호
# # 가능한 한 다양한 초밥
# # 벨트!!
#
# def dish(idx):
#     global max_dish, cnt
#     # 조기 종료: 가장 최대를 구했다면
#     if max_dish == k + 1:
#         return
#     # 종료: 벨트 한바퀴 다 돌았을 때
#     if idx == N:
#         return
#     # 초밥 개수 구하기
#     eat = set(lst[idx:idx+k])
#     if c in eat:
#         cnt = len(eat)
#     else:
#         cnt = len(eat) + 1
#
#     max_dish = max(cnt, max_dish)
#
#     dish(idx+1)
#
N, d, k, c = map(int, input().split())
lst = list(int(input()) for _ in range(N))

lst = lst + lst[:k]
max_dish = 0
cnt = 0
#
# dish(0)
# print(max_dish)


# 왜 위에꺼는 안되고 이게 되노 ㅅㅂ
for idx in range(N+1):
    eat = set(lst[idx:idx+k])
    if c in eat:
        cnt = len(eat)
    elif c not in eat:
        cnt = len(eat) + 1
    elif max_dish == k + 1:
        break

    max_dish = max(cnt, max_dish)

print(max_dish)