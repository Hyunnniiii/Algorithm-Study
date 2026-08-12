# 1 N극 / 2 S극
for T in range(1, 11):
    size = int(input())    # 항상 100
    arr = [list(map(int, input().split())) for _ in range(size)]

    # 하나의 열에서 1 다음에 2가 오면 교착 상태
    lst = []
    for col in range(size):
        crash = 0
        for row in range(size):
            # 1이 온다면
            if arr[row][col] == 1:
                start = row

                for new_row in range(start+1, size):
                    # 그 다음에 1이 또 오면 다시 시작
                    if arr[new_row][col] == 1:
                        break
                    # 2가 오면 교착 +1
                    elif arr[new_row][col] == 2:
                        crash += 1
                        break
                    # 0이 오면 패스
                    else:
                        pass
        lst.append(crash)
    print(f'#{T} {sum(lst)}')


