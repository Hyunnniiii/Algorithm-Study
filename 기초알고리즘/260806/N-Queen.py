# 하나의 행에 1개씩만 놓음
# 행에 하나 두고 -> 그 다음 행에서 되는거 선택 반복

def nqueen(idx):    # idx: 행 번호
    global cnt
    # 종료: N개 모두 놓았을 때
    if idx == N:
        cnt += 1
        return
    # 퀸 놓기
    for j in range(N):
        if v1[j] == 0 and v2[idx + j] == 0 and v3[idx - j] == 0:
            v1[j] = v2[idx + j] = v3[idx - j] = 1
            nqueen(idx+1)
            v1[j] = v2[idx + j] = v3[idx - j] = 0

for T in range(1, int(input())+1):
    N = int(input())

    v1 = [0]*N  # 방문한 열 표시
    v2 = [0]*2*N    # 대각선1 (/)
    v3 = [0]*2*N    # 대각선2 (\)

    cnt = 0     # 가능한 경우의 수

    nqueen(0)
    print(f'#{T} {cnt}')