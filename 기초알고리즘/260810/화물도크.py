# 최대 몇 대의 화물차가 이용할 수 있는지 알아내기
for TC in range(1, int(input()) + 1):
    N = int(input())
    time_table = [list(map(int, input().split())) for _ in range(N)]

    # 종료 시간이 가장 빠른 작업부터 선택
    # 종료 시간을 기준으로 정렬
    time_table.sort(key = lambda x: x[1])

    cnt = 0
    while time_table:
        start, end = time_table[0][0], time_table[0][1]
        cnt += 1
        time_table.pop(0)

        # 다음 트럭의 시작 시간이 이전 트럭 종료 시간보다 이전이면 선택X
        # 제거하다가 리스트 끝나면 종료
        while time_table and time_table[0][0] < end:
            time_table.pop(0)

    print(f'#{TC} {cnt}')
