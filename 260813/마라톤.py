# N개의 체크포인트가 있는데 ''1과 N번째를 제외하고'' 최대 하나만 건너뛴다
# 안 건너뛰는게 이득일수도
# 여러 체크포인트가 동일한 위치에 있을 수도 있다
# 달려야 하는 최소 거리 찾기
# 출력 끝에 줄바꿈 문자??

# 3 <= N <= 100,000인데 이거 노가다가 되나
N = int(input().strip())
min_length = float('inf')
lst = [list(map(int, input().split())) for _ in range(N)]
start_x, start_y = lst[0][0], lst[0][1]

# 체크포인트를 하나씩 빼가면서 거리를 계산
for k in range(1, N-1):
    length = 0
    a = lst[k]  # 다시 복구할거임
    del lst[k]

    for i in range(1, N-1):
        nxt_x, nxt_y = lst[i][0], lst[i][1]    # 다음 체크포인트
        length += abs(start_x - nxt_x) + abs(start_y - nxt_y)

        start_x, start_y = nxt_x, nxt_y

    min_length = min(length, min_length)
    lst.insert(k, a)    # 복구
    start_x, start_y = lst[0][0], lst[0][1]


# 체크포인트를 모두 거친 경우
all_length = 0
start_x, start_y = lst[0][0], lst[0][1]
for i in range(1, N):
    nxt_x, nxt_y = lst[i][0], lst[i][1]
    all_length += abs(start_x - nxt_x) + abs(start_y - nxt_y)

    start_x, start_y = nxt_x, nxt_y

ans = min(min_length, all_length)
print(ans)