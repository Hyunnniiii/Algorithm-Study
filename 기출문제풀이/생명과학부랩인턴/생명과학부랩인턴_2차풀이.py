
""" 생명과학부 랩 인턴 / 20260926 하루 종일 졸림 / 체감 난이도: 실버
소요 시간 35분 / 시도 1회 / 실행 시간 330ms (코드트리) / 메모리 26MB (코드트리)

1차 풀이에서는 딕셔너리를 안쓰고 배열에 모든 정보를 집어넣었다.
오늘은 당연히 딕셔너리를 썼는데..  이유는 일단 정보가 3개고, 크기가 서로 다르다고 해줬고 (이게 아주 개꿀)
매번 배열 순회하면서 곰팡이 나오면 이동 처리하는 방식이 비효율적일 것 같아서.
딕셔너리만 순회하려고 썼다.
그리고 방향도 입력에서 주는 순서대로 안하고 반대 방향 바꾸기 편하게 입력 단계에서 바꿔줬다. 굳
이전에 비해 코드가 아주 깔끔해서 좋다. 우하하

아쉬운 점은 문제 조건에 (0<=s<=1000) 이라고 되어있는데 내가 한칸씩 이동하게 했다는 것..
1000번 다 이동하고 앉아있을거냐고. 문제에서 주는 변수들의 범위를 잘 보자.

"""

# 14:25 시작 ~ 14:36 손구상 완 ~ 14:46 주석 설계 완 ~ 15:00 구현
# 구할 것: 채취한 곰팡이 크기의 총합
# ===================

import sys
sys.stdin = open('../input.txt', 'r')

# [0] 범위
def in_range(nr,nc):
    return 0<=nr<R and 0<=nc<C


# [1] 처음 만난 곰팡이 죽이기
def find_pang(col):
    global ans

    for row in range(R):
        if arr[row][col] == 0:
            continue
        ans += arr[row][col]
        pang.pop(arr[row][col])
        arr[row][col] = 0
        break


# [2] 곰팡이 이동하기
def move_pang():
    global arr

    imsi = [[0]*C for _ in range(R)]
    to_remove = []      # 삭제할 곰팡이 크기값 넣어주기

    for key, info in pang.items():
        sr, sc, sv, sd = info

        r, c, v, d = sr, sc, sv, sd

        # 속력 범위가 매우 크니까 줄여주자
        if d==0 or d==2:
            v = sv % (2*(R-1))
        elif d==1 or d==3:
            v = sv % (2*(C-1))

        # 가세요
        for k in range(v):
            nr, nc = r+dr[d], c+dc[d]

            if not in_range(nr,nc):
                d = (d+2)%4
                nr, nc = r+dr[d], c+dc[d]
            r, c = nr, nc

        if imsi[r][c] == 0:
            imsi[r][c] = key
            pang[key] = (r, c, v, d)
        elif imsi[r][c] < key:
            to_remove.append(imsi[r][c])
            imsi[r][c] = key
            pang[key] = (r,c,v,d)
        elif imsi[r][c] > key:
            to_remove.append(key)

    for key in to_remove:
        pang.pop(key)

    arr = imsi


def debug_print(word):
    if DEBUG:
        print('==========')
        print(word)
        print('배열 내 위치 확인')
        for row in arr:
            print(row)
        print()
        print('곰팡이 현황')
        print(pang)
        print()

DEBUG = False
###########################
R, C, K = map(int, input().split())
arr = [[0]*C for _ in range(R)]
pang = {}   # {크기 : (행, 열, 속력, 방향)}
change = [None, 0, 2, 1, 3]

for _ in range(K):
    x,y,s,d,b = map(int, input().split())
    d = change[d]
    arr[x-1][y-1] = b
    pang[b] = pang.get(b, (x-1, y-1, s, d))

debug_print('입력 확인')

# 상우하좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

# 실행부
ans = 0
for col in range(C):
    # [1] 열 탐색, 처음 만난 곰팡이 죽이기
    find_pang(col)
    debug_print('곰팡이 채취 완료')

    # 곰팡이 다 사라졌으면 끝
    if len(pang) == 0:
        break

    # [2] 곰팡이 이동하기
    move_pang()
    debug_print('곰팡이 이동 완료')

print(ans)
