
# 1. 몬스터 복제 시도
# 현재 칸에 자신과 같은 방향을 가진 알을 복제

# 2. 몬스터 이동
# 알이 아닌 몬스터만 한 칸 이동
# 이동 불가: 몬스터 시체가 있거나, 팩맨이 있거나, 범위 밖
# 이동이 불가한 경우 반시계로 45도 회전해가면서 갈 수 있는 방향 확인, 다 안되면 제자리

# 3. 팩맨 이동
# 총 3칸을 이동. 상좌하우 우선순위
# 64가지 선택지 중 가장 많은 몬스터 먹고, 우선순위에 따른 방향을 선택
# 이동 과정 중 격자 범위를 벗어날 수는 없다
# 이동하면서 만나는 몬스터만 먹는다. 알은 안먹음
# 움직이기 전에 함께 있었던 몬스터 먹지 않는다 >> 뭔소리임?
# 시작점에 있는 몬스터는 먹지 않는다는 소리로 간주할게?????

# 4. 몬스터 시체 소멸
# 시체는 2턴동안 유지
# 이거 생기고 나서 한 턴 지나면 1턴인건가? 확인해

# 5. 몬스터 복제 완성
# 방향 유지하고 알 부화

# 구할 것: 모든 턴 진행 후 남은 살아있는 몬스터의 수

# 한 칸에 여러 몬스터, 여러 알, 여러 시체 존재 가능
# 이거 몬스터의 idx 필요한가? > NO
# 만약 팩맨이 있는 자리에 알이 있는데 그 다음에 부화한다면? > 먹지 말래
# 동시 처리 필요한 것이 있는가? > 그냥 각 단계 나눠서 잘 구현하면 될듯
# 입력받을 때 행, 열, 방향 1씩 빼라

# ==================
# 딕셔너리를 계속 잘못 쓴다
# 리스트 순회하면서 리스트 수정하지 마라
# visit 백트래킹 처리. 입력할 때 [sr, sc]로 visit에 저 시작점을 포함하고 시작하면 안됨
# 시간초과 남 ..
#

# ========================================

# import time
# start = time.time()

## 입력
M, T = map(int, input().split())
pack_r, pack_c = map(lambda x : int(x)-1, input().split())

monster = [[[] for _ in range(4)] for _ in range(4)]
for _ in range(M):
    r, c, d = map(lambda x : int(x)-1, input().split())
    monster[r][c].append(d)

# 알, 시체는 dict로 해볼게 근데 시체가 영어로 뭐더라
# 알: (행,열,방향) / 시체: (행,열)
egg = {}
dead = {0 : [], 1 : [], 2 : []}     # 1은 1일 남은거, 2는 2일 남은거

# 방향
di = [-1,-1,0,1,1,1,0,-1]
dj = [0,-1,-1,-1,0,1,1,1]

# 범위
def in_range(ni, nj):
    return 0 <= ni < 4 and 0 <= nj < 4


# 함수 1: 몬스톼 복쪼ㅒ
# 몬스터 배열을 순회하면서 본인과 같은 방향을 egg에 추가한다
def duplicate():
    for row in range(4):
        for col in range(4):
            if len(monster[row][col]) > 0:
                for mon_dir in monster[row][col]:
                    # 딕에 없으면 만들어
                    if (row, col) not in egg.keys():
                        egg[(row, col)] = [mon_dir]
                    # 딕에 있으면 그냥 추가
                    else:
                        egg[(row,col)].append(mon_dir)


# 함수 2: 몬스터 이돵
def move():
    to_put = []
    to_remove = []
    for r in range(4):
        for c in range(4):
            if len(monster[r][c]) > 0:

                for mon in monster[r][c]:
                    for _ in range(8):
                        nr, nc = r + di[mon], c + dj[mon]

                        if in_range(nr, nc) and((nr, nc) not in dead[0]) and ((nr, nc) not in dead[1]) and\
                                ((nr, nc) not in dead[2]) and not (nr == pack_r and nc == pack_c):
                            to_put.append([nr, nc, mon])
                            to_remove.append([r, c])
                            break

                        else:
                            mon = (mon + 1) % 8

    # 다 처리했으면 몬스터 배열에서 삭제하고 다시 집어 느
    for lst in to_remove:
        monster[lst[0]][lst[1]] = []
    for lst in to_put:
        monster[lst[0]][lst[1]].append(lst[2])


# 함수 3: 팩맨 이동
def kill(si, sj, cnt, remove_lst, visit):     # 현재 위치, 죽인 몬스터 수, 죽일 곳의 좌표
    global max_kill, real_kill_lst

    # 종료: 3칸 모두 이동
    if len(remove_lst) == 3:
        if cnt > max_kill:
            max_kill = cnt
            real_kill_lst = remove_lst
        return

    # 4개 방향 중 하나 선택해서 이동
    # 몬스터 있으면 죽이고 시체 좌표 저장하기. 범위 벗어난 곳은 불가능
    for k in range(0,4):
        ni, nj = si + di[k*2], sj + dj[k*2]

        if in_range(ni, nj) and [ni, nj] in visit:
            kill(ni, nj, cnt, remove_lst + [(ni,nj)], visit)

        elif in_range(ni, nj) and [ni, nj] not in visit:
            kill(ni, nj, cnt + len(monster[ni][nj]), remove_lst + [(ni, nj)], visit + [[ni, nj]])


# 함수 4: 몬스터 시체 소멸, 알 부화
def new():
    global dead, egg

    # 몬스터 시체 소멸하기
    # 1에 있는 애들 다 삭제하고 2에 있는 애들 1로 옮겨
    new_dead = {0:[], 1:[], 2:[]}
    new_dead[1] = dead[2]
    new_dead[0] =dead[1]

    dead = new_dead

    # 알 부화하기 > 다 부화하면 알 정보 초기화
    for coord, my_dir in egg.items():
        x, y = coord[0], coord[1]
        for mons in my_dir:
            monster[x][y].append(mons)

    egg = {}


## 실행
for _ in range(T):
    duplicate()
    move()

    max_kill = -float('inf')
    real_kill_lst = []  # 죽일 곳 좌표 모음
    kill(pack_r, pack_c, 0, [], [])

    for lst in real_kill_lst:
        row, col = lst[0], lst[1]
        if len(monster[row][col]) > 0 and not (pack_r == row and pack_c == col):
            dead[2].append((row, col))
            monster[row][col] = []

    pack_r, pack_c = real_kill_lst[-1][0], real_kill_lst[-1][1]

    new()

# 정산
ans = 0
for r in range(4):
    for c in range(4):
        ans += len(monster[r][c])
print(ans)

# end = time.time()
# print(end-start)