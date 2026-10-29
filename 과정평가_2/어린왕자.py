from collections import deque

for TC in range(1, int(input())+1):
    N, M = map(int, input().split())    # N행 M열

    # 0 빈칸 / 1 나무 -> 0만 지나갈 수 있음
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    cnt = 0   # 구역의 개수
    area_lst = []   # 영역 크기 저장할 리스트

    for i in range(N):
        for j in range(M):

            # 0이 나오면 영역 카운트 시작
            if arr[i][j] == 0:
                arr[i][j] = 1
                to_go = deque([(i, j)])

                cnt += 1
                area = 1    # 영역의 크기

                while to_go:
                    si, sj = to_go.popleft()

                    for k in range(4):
                        # 넘어가는 영역 처리
                        ni = (si + di[k]) % N
                        nj = (sj + dj[k]) % M

                        if arr[ni][nj] == 0:
                            area += 1
                            arr[ni][nj] = 1
                            to_go.append((ni, nj))

                area_lst.append(area)
    if area_lst:
        print(f'#{TC} {cnt} {min(area_lst)} {max(area_lst)}')
    else:    # 영역이 한개도 없을 수 있다
        print(f'#{TC} 0 0 0')