# C, R = map(int, input().split())    # R행 C열
# N = int(input())    # 자르는 횟수
# cut_list = [list(map(int, input().split())) for _ in range(N)]
#
# # 가로 0, 세로 1
# lst = [[R, C]]    # 행x열 정보 저장할 리스트
# for i in range(N):
#     # 가로로 자를 때: 가로 길이 그대로, 세로 길이 2개로 나눈다
#     if cut_list[i][0] == 0:
#         for _ in range(i+1):
#             row, col = lst.pop(0)
#             lst.append([cut_list[i][1],col])
#             lst.append([row-cut_list[i][1], col])
#
#     # 세로로 자를 때: 세로 길이 그대로, 가로 길이 2개로 나눈다
#     else:
#         for _ in range(i+1):
#             row, col = lst.pop(0)
#             lst.append([row, cut_list[i][1]])
#             lst.append([row, col-cut_list[i][1]])
# print(lst)
# max_jongee = 0
# for x in lst:
#     if x[0]*x[1] > max_jongee:
#         max_jongee = x[0]*x[1]
# print(max_jongee)

# 접근이 잘못됨
# 같은 방향으로 2번 자르면 그 사이에 낀 애 길이가 이상해짐 전체에서 빼버리니까

# 자르는 위치를 저장하고 인접한 차이들의 곱 중 최대를 구한다
C, R = map(int, input().split())    # R행 C열
N = int(input())    # 자르는 횟수
cut_list = [list(map(int, input().split())) for _ in range(N)]

G = [0]  # 가로
S = [0]  # 세로
for x in cut_list:
    # 가로로 자를 때
    if x[0] == 0:
        G.append(x[1])
    # 세로로 자를 때
    else:
        S.append(x[1])
G.append(R)
S.append(C)

# 자르는 위치 순서대로 정렬
G.sort()
S.sort()

# 잘린 종이 넓이 구하기
lst = []
for x in range(len(G)-1):
    for y in range(len(S)-1):
        lst.append((G[x+1]-G[x])*(S[y+1]-S[y]))
print(max(lst))