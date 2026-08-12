# 0 <= N <= 100,000 / 0 <= K <= 100,000
#
# N, K = map(int, input().split())    # N 도훈 -> K 재우
#
# q = [N]
# cnt = 0
#
# # K를 잡을 때까지 반복
# following = True
# while following:
#     for i in range(len(q)):
#         dohun = q.pop(0)
#
#         # 3개 방향
#         q.append(dohun + 1)
#         q.append(dohun - 1)
#         q.append(dohun * 2)
#     cnt += 1
#
#     if K in q:
#         following = False
# print(cnt)

# ============ 시간 초과 뜸

# 0 <= N <= 100,000 / 0 <= K <= 100,000
# from collections import deque
#
# N, K = map(int, input().split())  # N 도훈 -> K 재우
#
# q = deque()
# q.append(N)
#
# visit = [0]*100001
# visit[N] = 1
#
# cnt = 0
# # if N == K:
# #     q= []
#
# # K를 잡을 때까지 반복
# while q:
#     for i in range(len(q)):
#         dohun = q.popleft()
#
#         # 다음 위치 추가 (기존에 구하지 않았던 숫자만)
#         a, b, c = dohun + 1, dohun - 1, dohun * 2
#         if K == a or K == b or K == c:
#             q = []
#             break
#
#         else:
#             for x in (a, b, c):
#                 if 0 <= x <= 100000 and not visit[x]:
#                     q.append(x)
#                     visit[x] = 1
#     cnt += 1
# print(cnt)

# ======= 예외처리 없이 하고 싶음

from collections import deque

N, K = map(int, input().split())  # N 도훈 -> K 재우

q = deque()
q.append(N)

visit = [0]*100001
cnt = 0

# K를 잡을 때까지 반복
while q:
    for i in range(len(q)):
        dohun = q.popleft()
        visit[N] = 1

        # N과 K가 같은지 비교
        if dohun == K:
            q = []
            break

        # 같지 않으면 다음 위치 추가 (기존에 구하지 않았던 숫자만)
        else:
            a, b, c = dohun + 1, dohun - 1, dohun * 2
            for x in (a,b,c):
                if 0 <= x <= 100000 and not visit[x]:
                    q.append(x)
                    visit[x] = 1
            cnt += 1
print(cnt)