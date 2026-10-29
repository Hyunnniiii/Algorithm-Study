
# [정리]
# 1. 주어진 공격 방향과 칸 수만큼 몬스터를 삭제 (칸 수는 제자리 제외)
# 2. 빈 공간만큼 나선형 앞으로 당기고 채우기
# 3. 반복해서 4번 이상 나오는 몬스터 삭제 >> '동시에'
# 4. 삭제 후 당겨서 채워주기 >> 더이상 4번 이상 반복 없을 때까지
# 5. 같은 숫자끼리 짝 지어서 (개수, 숫자)로 바꿔서 넣어주기
# 6. 점수: 삭제되는 몬스터 번호 x 개수

# [주의]
# 삭제 동시에 진행, 0 부분 당겨준 다음에 다시 동시에 삭제 진행
# 배열 범위 넘어가면 나머지는 무시

# =======================

## 입력 받기
N, M = map(int, input().split())
mirro = [0] * (N*N-1)

arr = [list(map(int, input().split())) for _ in range(N)]

# 우하좌상
di = [0,1,0,-1]
dj = [1,0,-1,0]

# 배열에서 달팽이 순서대로 1차원 리스트에 넣기
# 1차원 리스트로만 풀거임
si, sj, sd, cnt = N//2, N//2-1, 2, 0
visit = [[0]*N for _ in range(N)]
visit[N//2][N//2] = 1
visit[si][sj] = 1
mirro[cnt] = arr[si][sj]

while True:
    cnt += 1
    sd = (sd-1)%4
    ni, nj = si + di[sd], sj + dj[sd]

    if visit[ni][nj] != 0:
        sd = (sd + 1)%4
        ni, nj = si + di[sd], sj + dj[sd]

    visit[ni][nj] = 1
    mirro[cnt] = arr[ni][nj]

    if ni == 0 and nj == 0:
        break

    si, sj = ni, nj


## 함수 만들기
# 1. 공격하라
def attack(d, p):   # 공격 방향 d, 공격 칸 수 p를 입력
    global ans
    idx = 1     # 몇 칸까지 공격했니
    if d == 0:      # 우
        while idx < p+1:
            ans += mirro[4 * (idx ** 2) + idx - 1]
            mirro[4*(idx**2) + idx - 1] = 0
            idx += 1

    if d == 1:      # 하
        while idx < p+1:
            ans += mirro[4 * (idx ** 2) - idx - 1]
            mirro[4*(idx**2) - idx - 1] = 0
            idx += 1

    if d == 2:      # 좌
        while idx < p+1:
            ans += mirro[4 * (idx ** 2) - (3 * idx) - 1]
            mirro[4*(idx**2) - (3*idx) - 1] = 0
            idx += 1

    if d == 3:      # 상
        while idx < p+1:
            ans += mirro[4 * (idx ** 2) + (3 * idx) - 1]
            mirro[4*(idx**2) + (3*idx) - 1] = 0
            idx += 1


# 2. 빈 공간 채우기
# 0이 나오면 제거 후 맨 뒤에 0 추가
def fill():
    idx = 0
    while idx < N*N-1:
        if mirro[idx] == 0:
            mirro.pop(idx)
            mirro.append(0)
        else:
            idx += 1

        if sum(mirro[idx:]) == 0:
            break


# 3. 4번 이상 반복되는 몬스터 삭제하기
# 언제 멈출래 > 0이 2번 이상 연속일 때
def fourkill():
    global ans
    idx = 0
    while idx < N*N - 2:
        if mirro[idx] == mirro[idx + 1] == 0:
            break

        if mirro[idx] == mirro[idx + 1] == mirro[idx + 2] == mirro[idx + 3]:
            to_kill, find_idx = mirro[idx], idx + 4
            ans += to_kill * 4
            mirro[idx:idx + 4] = [0] * 4

            while True:
                if mirro[find_idx] == to_kill:
                    ans += to_kill
                    mirro[find_idx] = 0
                    find_idx += 1
                else:
                    idx = find_idx
                    break
        else:
            idx += 1


# 4. 짝 지어주기
# 어차피 최대 3번 연속이니까.. 그냥 케이스 나눠서 진행
def zzak():
    idx, nidx = 0, 0
    nlst = [0] * (N*N-1)
    while nidx < N*N-1:
        # 0 등장하면 멈춰
        if mirro[idx] == 0:
            break

        # 1번만 있을 때
        if mirro[idx] != mirro[idx+1]:
            nlst[nidx], nlst[nidx+1] = 1, mirro[idx]
            idx += 1

        # 2번 연속
        elif mirro[idx] == mirro[idx+1] and mirro[idx] != mirro[idx+2]:
            nlst[nidx], nlst[nidx+1] = 2, mirro[idx]
            idx += 2

        # 3번 연속
        elif mirro[idx] == mirro[idx + 1] == mirro[idx+2] and mirro[idx] != mirro[idx + 3]:
            nlst[nidx], nlst[nidx + 1] = 3, mirro[idx]
            idx += 3
        nidx += 2

    return nlst


## 실행
ans = 0
for _ in range(M):
    d, p = map(int, input().split())

    attack(d, p)
    fill()

    status = True
    while status:
        fourkill()
        fill()
        for idx in range(N*N-4):
            if mirro[idx] == mirro[idx+1] == mirro[idx+2] == mirro[idx+3] and mirro[idx] != 0:
                break
            idx += 1

        if idx == N*N-4 and status:
            break

    mirro = zzak()

print(ans)









