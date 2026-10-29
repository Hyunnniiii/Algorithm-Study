# 15:47 시작르
# 16:05 구상완
# 17:22 일단 다 했는데 틀림
# 18:50 다시 시작
# 19:39 1차 제출 > 시작점 ㅋㅋ
# 19:45 성공 but 난 이미 너무 지치고 병들었다

# 행/열 중에서 개수가 많은 방향에 대해 선택. 개수 같으면 행.
# 만약 행을 선택했다 치면
# ㄴ 출현 빈도 순으로 행 정렬. 각 숫자 옆 칸에 출현 횟수 넣어주기
# ㄴ 출현 빈도 같으면 > 크기 순 정렬

# 불가능하다는걸 어떻게 알지? > 그냥 100번 넘어가면 종료로 해야할듯

# 구할 것: arr[r][c]가 k가 되기 위한 최소 시간
# 이때 불가능하거나, 100초를 초과하면 -1 출력

# 주의: r, c가 1부터 시작하므로 처리해줘야 함
# import pprint
# import time
# start = time.time()


## 입력 받기
ans_r, ans_c, ans_k = map(int, input().split())
arr = [[0]*100 for _ in range(100)]
for i in range(3):
    input_lst = list(map(int, input().split()))
    arr[i][0], arr[i][1], arr[i][2] = input_lst

## 이게 왜 놀이임? 짜증나죽겠네
tot_time = 0
status = True

# 이미 된다면?
if arr[ans_r-1][ans_c-1] == ans_k:
    print(tot_time)
    status = False

max_row_len, max_col_len = 3, 3
for T in range(100):
    # [0] 시작
    tot_time += 1
    row_len, col_len = max_row_len, max_col_len

    # 이미 정답이었다면
    if status == False:
        break

    ## [1] 행의 길이가 더 길 때
    if row_len >= col_len:

        # [2] 행에 대해 숫자 세고 리스트로 생성
        max_col_len = 0
        # 하나의 행에 대해 진행
        for i in range(row_len):
            row_lst = []
            for j in range(col_len):
                row_lst.append(arr[i][j])

            row_Q = []

            row_lst.sort(reverse=True)
            cur_num, cnt = row_lst[0], 0
            # (숫자, 개수) 튜플 큐에 넣어주기
            for x in range(len(row_lst)):
                if row_lst[x] == 0:
                    break
                if row_lst[x] == cur_num:
                    cnt += 1
                else:
                    row_Q.append((cur_num, cnt))
                    cnt = 1
                    cur_num = row_lst[x]
            # 마지막 숫자
            if cur_num != 0:
                row_Q.append((cur_num, cnt))


            # [3]  생성한 리스트를 배열에 새로 넣어주기
            row_Q.sort(key=lambda X: (X[1], X[0]))
            if len(row_Q) > 50:
                row_Q = row_Q[:50]
            idx = 0
            for x,y in row_Q:
                arr[i][idx], arr[i][idx+1] = x, y
                idx = (idx+2)%100

            # 뒤쪽에 0이 아닌 것이 남아있으면 지우기
            for erase in range(2*len(row_Q), 100):
                if arr[i][erase] != 0:
                    arr[i][erase] = 0

            # 최대 길이 갱신하기
            max_col_len = max(max_col_len, len(row_Q) * 2)

    ## [1] 열의 길이가 더 길 때
    if row_len < col_len:

        # [2] 열에 대해 숫자 세고 리스트로 생성
        max_row_len = 0

        for j in range(col_len):
            col_lst = []
            for i in range(row_len):
                col_lst.append(arr[i][j])

            col_Q = []
            col_lst.sort(reverse=True)
            cur_num, cnt = col_lst[0], 0

            for x in range(len(col_lst)):
                if col_lst[x] == 0:
                    break
                if col_lst[x] == cur_num:
                    cnt += 1
                else:
                    col_Q.append((cur_num, cnt))
                    cnt = 1
                    cur_num = col_lst[x]
            if cur_num != 0:
                col_Q.append((cur_num, cnt))

            # [3]  생성한 리스트를 배열에 새로 넣어주기
            col_Q.sort(key=lambda X: (X[1], X[0]))

            if len(col_Q) > 50:
                col_Q = col_Q[:50]
            idx = 0
            for x,y in col_Q:
                arr[idx][j], arr[idx+1][j] = x, y
                idx = (idx+2)%100
            for erase in range(2*len(col_Q), 100):
                if arr[erase][j] != 0:
                    arr[erase][j] = 0

            # 최대 길이 갱신해주기
            max_row_len = max(max_row_len, len(col_Q) * 2)

    # [4] 달성했는지 확인
    if arr[ans_r-1][ans_c-1] == ans_k:
        print(tot_time)
        break

if arr[ans_r-1][ans_c-1] != ans_k:
    print(-1)
#
# end = time.time()
# print(end - start)