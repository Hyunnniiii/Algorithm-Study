# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     S = list(map(int, input().split()))
#
#     lst = []
#
#     for num in S:
#         for j in range(len(lst)):
#             if num < lst[j]:
#                 lst.insert(j, num)
#                 break
#         else:
#             lst.append(num)
#
#     print(f'#{test_case}', *lst)

# =====================================

# lst = []
# for _ in range(9):
#     lst.append(int(input()))
#
# found = False
#
# for i in range(9):
#     for j in range(i+1, 9):
#         if sum(lst)-lst[i]-lst[j] == 100:
#             a=lst[i]
#             b=lst[j]
#             found=True
#             break
#     if found:
#         break
#
# lst.remove(a)
# lst.remove(b)
# for x in lst:
#     print(x)

# ======================

# N, M = map(int, input().split())
# cards = list(map(int, input().split()))
# lst = []
# max_sum = 0
#
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             sum = cards[i]+cards[j]+cards[k]
#
#             if max_sum < sum <= M:
#                 max_sum = sum
#
# print(max_sum)
#
# =======================
#
# for test_case in range(1, int(input()) + 1):
#
#     N = int(input())
#     success = False
#     for j in range(N):
#         S = list(map(str, input()))
#         num = 0
#
#         for i in range(N-1):
#             if S[i] == S[i+1] == 'o':
#                 num += 1
#             else:
#                 continue
#
#             if num == 4:
#                 print(f'#{test_case}', 'YES')
#                 success = True
#                 break
#             else:
#                 continue
#
#     if success != True:
#         print(f'#{test_case}', 'NO')
#
# ======================
# for test_case in range(1, int(input()) + 1):
#
#     N = int(input())
#     lst = [[0] * N for _ in range(N)]
#
#     for i in range(N):
#         S = list(map(str, input()))
#         for k in range(N):
#             if S[k] == 'o':
#                 lst[i][k] = 1
#
#     arr = [0]*N
#     for j in range(N):
#         for k in range(N):
#             arr[j] += lst[j][k]
#     print(arr)


# ===============

# for test_case in range(1, int(input()) + 1):
#
#     N = int(input())
#     A = list(map(int, input()))
#     for i in range(N):
#         lst = []
#         num = 1
#
#         for j in range(len(A)-1):
#             if A[j] == A[j+1] == 1:
#                 num += 1
#             else:
#                 lst.append(num)
#                 num = 1
#             lst.append(num)
#     if max(lst) == 1:
#         print(f'#{test_case}', 1)
#     else:
#         print(f'#{test_case}', max(lst))

# for test_case in range(1, int(input())+1):
#
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     tot = 0
#     di = [-1,1,0,0]
#     dj = [0,0,-1,1]
#     for i in range(N):
#         for j in range(N):
#             for k in range(4):
#                 ni, nj = i + di[k], j + dj[k]
#
#                 if 0 <= ni < N and 0 <= nj < N:
#                     sm = abs(arr[i][j]-arr[ni][nj])
#                     tot += sm
#
#     print(f'#{test_case}', tot)