
def dice(n, alst):
    # 종료조건
    if n == N:
        print(*alst)
        return
    # 하부함수
    for j in range(1,7):
        dice(n+1, alst + [j])

for T in range(1, int(input())+1):
    N = int(input())
    print(f'#{T}')
    dice(0, [])

# =================
# =================
# # n: 지금까지 주사위를 던진 횟수 / alst: 지금까지 나온 주사위 숫자들
# def dfs(n, alst):
#     # 1. 종료조건: n에 관련
#     if n == N:
#         print(*alst)
#         return
#     # 2. 하부함수 호출
#     for j in range(1,7):
#         dfs(n+1, alst + [j])
#
# for T in range(1, int(input())+1):
#     N = int(input())
#     print(f'#{T}')
#     dfs(0, [])