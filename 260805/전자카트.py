# 구역을 1번씩만 방문, 마지막에 사무실로 복귀
# 100이하의 자연수, 3<=N<=10

def golf(row, sm, cnt):
    global min_battery
    # 종료조건: N-1번 방문 -> 마지막 1열 더하기
    if cnt == N-1:
        sm += arr[row][0]
        min_battery = min(min_battery, sm)
        return

    # 구역 정하기
    # 대각선은 방문X / 0행 시작, 0열 도착으로
    for col in range(N):
        if v[col] == 0 and col != row and col != 0 :
            v[col] = 1
            golf(col, sm + arr[row][col], cnt + 1)
            v[col] = 0

for T in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*N   # 방문한 열 표시

    min_battery = 100*N + 1
    golf(0,0,0)
    print(f'#{T} {min_battery}')

