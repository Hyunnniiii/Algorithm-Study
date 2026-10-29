
''' 미로 타워 디펜스 / 20260907 / 체감 난이도 : 골드 4
소요 시간:  / 시도: 1회 / 실행 시간: 207ms (코드트리) / 메모리: 20MB

[타임라인]
09:04 - 09:43(40분) 문제 읽기 / 입력 받기 / 구상
09:43 - 11:00 (77분) 구현
11:00 - 11:04 (4분) 엣지 확인, 제출

[구상]
- (good)
    - 드디어 옆자리 사람들이 손구상한다!!!!! 같이 구상하고 있으니 안정감이 느껴진다.
    - 그래서 그런지 지금까지 풀었던 문제들에 비해 구상이 오래 걸렸음에도 완벽하게 끝날 때까지
    신경쓰지 않고 진행할 수 있었다.. 뭐 이전에도 그냥 하긴 했는데 아무튼 구상할 때 서두르지 말자
    - 문제를 읽자마자 1차원 리스트로 풀면 편하겠다는 생각이 들었다. 기막힌 발상이라고
    생각했는데 다들 그렇게 풀었더라..

- (bad)
    - 숫자 입력이 배열 형태로 나오는걸 구상 거의 다 하고나서 알았다. 달팽이 안하고 싶어서
    1차원 배열 생각해냈는데, 결국 해야된다는걸 구현 시작하려다가 깨달음.. 인풋 보면서 구상하라고
    - 사실 구상할 때 상하좌우 공격 방향 인덱스를 점화식으로 다 구하느라 구상이 오래 걸렸다.
    솔직히 시험 당일 긴장되는 상황에서도 점화식을 내가 차분히 구할 수 있을지는.. 미지수라고 생각한다.

[구현]
- (good)
    - 짝지어주기 함수의 경우 최대 3번 뿐이라 그냥 일일히 다 썼는데, 이거 나쁘지 않은 것 같다.
    괜히 일반화한다고 규칙 찾다가 엣지 걸리지 말고 내가 감당할 수 있는 정도의 코드 길이면
    무식하단 생각이 들어도 그냥 쓰자.

- (bad)
    - 달팽이하기 싫어서 다른 방법 있나 한참 생각함. 너 구현할 때 호불호 가리지 마
    - 그리고 좀 느린가 싶기도 하고.. 검증할 시간 정말 최소 1시간은 확보하고 싶다

[디버깅]
    - 함수화 최고. 어느 단계에서 잘못됐는지 확인하기 정말 좋다. 그리고 함수 하나만
    떼어와서 다른 창에서 그 함수만 돌려볼 수 있으니까 정말.. 편하다
    분명 예전에 이걸 팁으로 들었던 기억이 나는데 그때는 이해하지 못했다 이제야 깨달았다

[후기]
    - 시간 많으니까.. 마음의 안정을 가지는게 제일 최고인 것 같다

---------------------------------------------------------
# [개선] 207ms > 88ms
# 달팽이 간소화
# 수학 계산 하지 말고 인덱스 배열을 만들어서 한번에 처리
# 24 23 22 21 20
#  9  8  7  6 19
# 10  1  C  5 18
# 11  2  3  4 17
# 12 13 14 15 16 >> 이런 식으로..

# ============================
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

# ======================='''


## 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr_idx = [[-1]*N for _ in range(N)]

# 우하좌상
di = [0,1,0,-1]
dj = [1,0,-1,0]

# 배열에서 달팽이 순서대로 1차원 리스트에 넣기
# 1차원 리스트로만 풀거임
i, j, d = N//2, N//2, 2
step = 1
mirro = []
go = True
while go:
    for _ in range(2):
        for _ in range(step):
            i += di[d]
            j += dj[d]
            arr_idx[i][j] = len(mirro)
            mirro.append(arr[i][j])

            if len(mirro) == N*N-1:
                go = False
                break

        if not go:
            break

        d = (d-1)%4
    step += 1

## 함수 만들기
# 1. 공격하라
def attack(d, p):   # 공격 방향 d, 공격 칸 수 p를 입력
    global ans

    sr, sc = N//2, N//2
    for dist in range(1, p+1):
        nr, nc = sr + di[d]*dist, sc + dj[d]*dist

        idx = arr_idx[nr][nc]
        ans += mirro[idx]
        mirro[idx] = 0


# 2. 빈 공간 채우기
# 0을 전부 제거하고 뒤에 부족한 개수만큼 0 채우면 됨
def fill():
    global mirro
    alive = [x for x in mirro if x != 0]
    mirro = alive + [0] * (N*N -1 - len(alive))


# 3. 4번 이상 반복되는 몬스터 삭제하기
# 죽일 몬스터가 있는지 여부를 리턴
def fourkill():
    global ans, mirro

    idx = 0
    nlst = []     # 안죽인 몬스터만 여기에 남길거임
    killed = False

    while idx < N*N - 1 and mirro[idx] != 0:
        num = mirro[idx]    # 현재 이 숫자 몇 번 반복되는가?
        cnt = 0     # 연속되는 횟수

        # 연속되는 같은 수 모두 포함
        while idx < N*N-1 and mirro[idx] == num:
            idx += 1
            cnt += 1

        # 4번 넘어가면 > 죽어
        if cnt >= 4:
            ans += num * cnt
            killed = True

        # 4번 안넘어간 몬스터는 보존
        else:
            nlst.extend([num]*cnt)

    mirro = nlst + [0] * (N*N-1 - len(nlst))

    return killed


# 4. 짝 지어주기
# 이것도 연속된거 한번에 처리해보자
def zzak():
    idx = 0
    nlst = []

    while idx < N*N-1 and mirro[idx] != 0:
        num = mirro[idx]
        cnt = 0

        while idx < N*N-1 and mirro[idx] == num:
            idx += 1
            cnt += 1

        nlst.extend((cnt,num))

        if len(nlst) >= N*N-1:
            break

    nlst = nlst[:N*N-1]
    nlst += [0]*(N*N-1 - len(nlst))

    return nlst


## 실행
ans = 0
for _ in range(M):
    d, p = map(int, input().split())

    attack(d, p)
    fill()

    while fourkill():
        pass

    mirro = zzak()

print(ans)









