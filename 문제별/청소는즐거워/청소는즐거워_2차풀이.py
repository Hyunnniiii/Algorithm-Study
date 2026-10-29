
""" 토스트 계란틀 / 20260917 / 체감 난이도: 실버
소요 시간 39분 / 시도 1회 / 실행 시간 299ms (코드트리) / 메모리 26MB (코드트리)

일단 과거의 내가 더 편하게 풀었다.
왜냐면 나는 합칠 계란에 대한 판정을 모두 완료한 뒤에 합쳐야 한다는 뭔가.. 지금까지 풀었던 문제들에
기반한 완료 후 처리 강박증에 빠진 나머지 그냥 bfs 돌리면서 한번에 처리해도 되는데 굳이 그룹별 정보를
딕셔너리에 받아서 따로 함수 구현해서 따로 처리해줬다.

근데 나쁜건 아닌 것 같음. 배열 갱신할 땐 항상 완료 후 처리!!!
종료 시점에 대한 처리는 이전보다 훨씬 편하게 했다.
엣지에 대한 것도 훨씬 잘 생각해냈으나 문제가 친절해서 다 알려줬다.. (0번째에 종료하는 경우)
"""

# 홀수 nxn 행렬. 정가운데에서 시작해서 나선형으로 바닥 청소
# [1] 빗자루 나선형에 맞춰서 이동
# [2] 이동한 위치의 먼지에 대해 정해진 비율에 따라 먼지 이동
# 이동한 위치의 먼지는 모두 없어진다

# 정가운데에는 먼지가 없는 상태로 시작
# 구할 것: 격자 밖으로 떨어진 먼지 양 총합
# ==============================

# 범위
def in_range(nr, nc):
    return 0<=nr<N and 0<=nc<N

###################################
N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]

# 방향별로 탐색할 곳
up = {1:((1,-1), (1,1)), 2:((0,-2),(0,2)), 5:((0,0), (-2,0)), 7:((0,-1),(0,1)),
      10:((-1,-1),(-1,1))}
down = {1:((-1,-1), (-1,1)), 2:((0,-2),(0,2)), 5:((0,0), (2,0)), 7:((0,-1), (0,1)),
        10:((1,-1),(1,1))}
left = {1:((-1,1), (1,1)), 2:((-2,0), (2,0)), 5:((0,0), (0,-2)), 7:((-1,0), (1,0)),
        10:((1,-1),(-1,-1))}
right = {1:((-1,-1), (1,-1)), 2:((-2,0), (2,0)), 5:((0,0), (0,2)), 7:((-1,0),(1,0)),
         10:((-1,1), (1,1))}

# 방향에 따라 딕셔너리 이름을 반환
change = [left, down, right, up]

# 4방향 (좌하우상)
dr = [0,1,0,-1]
dc = [-1,0,1,0]

# 실행부
ans = 0
sr, sc, sd = N//2, N//2, 0
for _ in range(N*N-1):
    # [1] 이동하기
    if (sr-sc==1 and sr<=N//2) or (sr+sc==N-1 and sr>N//2) or \
            (sr==sc and sr>N//2) or (sr+sc==N-1 and sr<N//2):
        sd = (sd+1)%4

    nr, nc = sr+dr[sd], sc+dc[sd]
    sr, sc= nr, nc
    print('이동 완료', sr, sc)
    # [2] 먼지 쓸기
    dust = arr[sr][sc]
    arr[sr][sc] = 0
    print(sr, sc)
    d_idx = change[sd]  # 현재 내가 진행 중인 방향 이름
    cur_sum = 0
    for percent, coords in d_idx.items():
        for ddr, ddc in coords:
            print('퍼센트, ddr,ddc',percent, ddr, ddc)
            # 5에 넣어준 00은 제외
            if percent==5 and ddr==0 and ddc==0:
                continue
            # 격자 안이면 > 배열에 더해준다
            if in_range(sr+ddr, sc+ddc):
                arr[sr+ddr][sc+ddc] += (dust*percent)//100
                cur_sum += (dust*percent)//100
                print(sr+ddr, sc+ddc, '에', (dust*percent)//100, '추가')
            # 벗어나면 > 정답에 더해준다
            else:
                ans += (dust*percent)//100
                cur_sum += (dust * percent) // 100
                print(sr+ddr, sc+ddc, '에', (dust*percent)//100, '추가')

        print('총합', cur_sum)
    # 다 했으면 내 바로 앞에 a% 추가
    a = dust - cur_sum
    if in_range(sr+dr[sd], sc+dc[sd]):
        arr[sr+dr[sd]][sc+dc[sd]] += a
    else:
        ans += a
    print('=== 청소 ===')
    for row in arr:
        print(row)
    print()

print(ans)