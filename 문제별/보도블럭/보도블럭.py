# 13:37 tlwkr
# 13:47 구상 완
# 14:00-14:02 장시르
# 14:47 1차 코딩 완
# 14:56 제출, 실패
# 15:26

# 놓지 않아도 갈 수 있는 경우가 있음!!
# 계단 길이가 1일 때 처리 해야지

# 일단 길이 L만큼 연속된 숫자가 있어야 함
# 탐색하다가 숫자가 바뀌면 카운트 시작
# 숫자 바뀌고 나서 L번 이상 바뀐 숫자가 안나오면 바로 X
# 바뀐 숫자가 1 차이가 아니면 X
# import pprint

## 입력받기
N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]   # 행 탐색
brr = list(zip(*arr))   # 열 탐색

## 확인하기
def block(arr):
    ans = 0

    # 한 줄씩 탐색
    for row in range(N):
        col = 0
        cur_num = arr[row][col]
        cnt = 1     # 어떤숫자가 연속되는 횟수 저장
        status = True

        while col < N-1 and status:

            # 그 다음 숫자가 바뀌지 않았다면
            if arr[row][col + 1] == cur_num:
                cnt += 1
                col += 1

            # 바뀌었다면: 1차이 나야한다
            else:
                ## 1 만큼 줄었을 때 > 그 다음 숫자가 L번 이상 나오는지 본다
                if cur_num - arr[row][col + 1] == 1:
                   # 다음 숫자부터 L번 나오는지 확인 시작
                   cnt = 1
                   col += 1
                   while status and cnt < L:
                       cur_num = arr[row][col]
                       if cur_num == arr[row][col+1]:
                           cnt += 1
                           col += 1
                       else:
                           status = False
                           break

                   if cnt == L:
                       if col + 1 == L:
                           break
                       cur_num = arr[row][col + 1]
                       cnt = 0


                # 1만큼 커졌을 때 > 지금까지 cnt가 L을 넘는지 확인
                elif arr[row][col] - arr[row][col + 1] == -1:

                    if cnt < L:
                        status = False
                        break

                    # L번 넘었다면:
                    else:
                        cur_num = arr[row][col+1]
                        col += 1
                        cnt = 1

                # 1차이 안난다면 > 불가능하므로 바로 종료
                else:
                    status = False
                    break

        # 다 끝날 때까지 break 안되면 설치 가능한 것
        if status:
            ans += 1

    return ans

print(block(arr)+block(brr))

