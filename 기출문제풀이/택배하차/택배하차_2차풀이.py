
""" 택배하차 / 20261006 거지같은 문제 / 체감 난이도: 골드5
소요 시간 ?분 / 시도 1회 / 실행 시간 209ms (코드트리) / 메모리 23MB (코드트리)

이 문제만 보면 화가 치밀어오름
그래 나 중력 회전 못한다
그냥 템플릿 외워줄게 외우니까 잘되고 좋네

"""
# 240시간 걸려도 푼다

def in_range(nr,nc):
    return 0<=nr<N and 0<=nc<N


def gravity():
    checked = set()
    for row in range(N-1, -1, -1):
        for col in range(N):
            if arr[row][col] in checked:
                continue

            if arr[row][col] > 0:
                box_idx = arr[row][col]
                sero, garo = box_info[box_idx]
                checked.add(box_idx)

                # 박스 좌표 모으기
                coord = []
                for r in range(row, row-sero, -1):
                    for c in range(col, col + garo):
                        coord.append((r,c))

                # 얼마나 내려갈 수 있는지 찾기
                move = 0
                while True:
                    status = True
                    for x, y in coord:
                        if not in_range(x+move, y):
                            status = False
                            break
                        if arr[x+move][y] > 0 and arr[x+move][y] != box_idx:
                            status = False
                            break
                    if not status:
                        break
                    move += 1

                # 기존 좌표 삭제
                for x, y in coord:
                    arr[x][y] = 0

                # 새로운 좌표에 박스 표시
                for x, y in coord:
                    arr[x+move-1][y] = box_idx


def debug_print(msg):
    if DEBUG:
        print('==', msg, '==')
        for row in arr:
            print(row)
        print()
        print(box_info)


########################
DEBUG = False
N, M = map(int, input().split())
arr = [[0]*N for _ in range(N)]
box_info = {}

# [0] 택배 처 넣기
for _ in range(M):
    idx, sero, garo, col = map(int, input().split())
    col -= 1
    box_info[idx] = (sero, garo)

    # 박스 좌표 리스트
    coord = []
    for r in range(0, sero):
        for c in range(col, col+garo):
            coord.append((r, c))

    # 얼마나 내릴 수 있는지 확인
    move = 0
    status = True
    while True:
        for x, y in coord:
            if not in_range(x+move, y):
                status = False
                break
            if arr[x+move][y] != 0:
                status = False
                break

        if not status:
            break
        move += 1

    # 구한 만큼 내리기
    for x, y in coord:
        arr[x+move-1][y] = idx

debug_print('입력 확인')

# 시작
while True:
    # 좌측 확인
    checked = set()     # 확인한 박스 idx 여기로
    hubo = []        # 삭제할 수 있는 박스 리스트
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 0:
                continue
            if arr[row][col] in checked:
                continue

            checked.add(arr[row][col])
            sero, garo = box_info[arr[row][col]]

            # 왼쪽 확인
            can_remove = True
            for left_row in range(row, row+sero):
                for left_col in range(col):
                    if arr[left_row][left_col] != 0:
                        can_remove = False
                        break
                if not can_remove:
                    break

            if can_remove:
                hubo.append(arr[row][col])
            break

    # 후보들 중 번호가 가장 작은 박스 삭제
    hubo.sort()
    box_info.pop(hubo[0])
    print(hubo[0])
    for r in range(N):
        for c in range(N):
            if arr[r][c] == hubo[0]:
                arr[r][c] = 0

    debug_print('왼쪽에서 삭제 완료')

    # 종료 확인
    if len(box_info) == 0:
        break

    # 중력
    gravity()

    debug_print('중력 적용 완료')

    # 우측 확인
    checked = set()  # 확인한 박스 idx 여기로
    hubo = []  # 삭제할 수 있는 박스 리스트
    for row in range(N):
        for col in range(N-1,-1,-1):
            if arr[row][col] == 0:
                continue
            if arr[row][col] in checked:
                continue

            checked.add(arr[row][col])
            sero, garo = box_info[arr[row][col]]

            # 오른쪽 확인
            can_remove = True
            for right_row in range(row, row+sero):
                for right_col in range(col+1, N):
                    if arr[right_row][right_col] != 0:
                        can_remove = False
                        break
                if not can_remove:
                    break

            if can_remove:
                hubo.append(arr[row][col])
            break

    # 후보들 중 번호가 가장 작은 박스 삭제
    hubo.sort()
    print(hubo[0])
    box_info.pop(hubo[0])
    for r in range(N):
        for c in range(N):
            if arr[r][c] == hubo[0]:
                arr[r][c] = 0

    debug_print('오른쪽 삭제 완료')

    # 종료 확인
    if len(box_info) == 0:
        break

    # 중력
    gravity()

    debug_print('중력 적용 완')
