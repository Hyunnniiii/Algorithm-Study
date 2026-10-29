
""" 보도블럭 / 20260922 / 체감 난이도: INF
소요 시간 INF / 시도 INF회 / 실행 시간 63ms (코드트리) / 메모리 17MB (코드트리)

와 진짜 능지 이슈로 난 이 문제가 너무 어려움. 0차 풀이인 것에는 이유가 있었음.
아 시키는 그대로 구현하는 문제 하고 싶다고!!!!!!! (그것도 잘 못함 캬캬)

아무튼.. 0차 풀이 & 1차 풀이 때 비슷하게 구상했다.
가로로 쫙 탐색하다가 숫자가 달라지면 > 그 지점에서 처리하는 방식이고,
포인터 써서 여태까지 같은 숫자였던 첫 블록(?) 표시해두고 그 포인터와 현재 내 위치 사이 거리가
L이 넘는지 확인하는 거였는데..
올라갈 때는 그게 되는데 내려갈 때가 안됨. 무한 굴레에 빠지게 되.

어렵다아아아아아아아ㅏ아아ㅏ아아아ㅏ아아ㅏ아아ㅏ아아아ㅏㅏㅏ아아ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ
또 풀어봐야지 뭐..

"""

# NxN 인도, 경사로 길이 L
# 경사로를 설치할거임
# 높이가 1 차이나는 보도블럭에 설치 가능, 낮은 칸에 설치
# 경사로 길이 L동안 바닥에 접촉해야 한다. 경사로가 놓인 보도블럭의 높이 같아야 함
# 불가한 경우: 높이 차이 1 초과, 경사로보다 짧은 바닥, 경사로 위에 경사로

# 구할 것: 지나갈 수 있는 열과 행의 총 개수
# ==================================

def search(arr, row):
    global ans

    visit = [0]*N
    for col in range(1, N):
        diff = arr[row][col] - arr[row][col-1]

        # 차이가 없으면 > 넘어가
        if diff == 0:
            continue

        # 1 증가하면 > 왼쪽으로 L칸 확인
        elif diff == 1:
            for k in range(1, L+1):
                nc = col-k

                # 범위 부족 > 불가
                if not 0<=nc<N:
                    return False

                # 높이가 달라짐 > 불가
                if arr[row][nc] != arr[row][col-1]:
                    return False

                # 이미 다른 경사로 사용 > 불가
                if visit[nc]:
                    return False

            # 여기까지 오면 가능 > visit에 사용 표시
            for k in range(1, L+1):
                visit[col-k] = 1

        # 1 감소하면 > 오른쪽으로 L칸 확인
        elif diff == -1:
            for k in range(L):
                nc = col + k

                # 범위 부족 > 불가
                if not 0<=nc<N:
                    return False

                # 다른 숫자 > 불가
                if arr[row][nc] != arr[row][col]:
                    return False

                # 이미 사용 > 불가
                if visit[nc]:
                    return False

            # 여기까지 왔으면 가능
            for k in range(L):
                visit[col+k] = 1

        # 이 외의 경우 > 불가능
        else:
            return False
    return True


N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
brr = [list(row[:]) for row in zip(*arr[::-1])]

ans = 0
for r in range(N):
    if search(arr, r):
        ans += 1
    if search(brr, r):
        ans += 1

print(ans)
