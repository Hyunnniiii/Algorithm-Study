# 인덱스 주의, 반대편 연결

# 1. 본인 방향, 속력만큼 이동
# 2. 하나의 칸에 2개 이상의 원자가 있는 경우 합성
# 2-1. 각각의 질량과 속력을 모두 합한다
# 2-2. 4개의 원자로 나눈다
# 2-3. 나눈 원자들을 해당 칸에서 질량/속력/방향 결정
# 질량: 질량합//5, 속력: 속력합//합친원자의개수, 방향: 합쳐지는 원자들 확인, 질량 0이면 소멸
# 이동 과정 중 만나는 것은 합성 아니다.

# 11:30 중단

# from pprint import pprint
## [0] 입력 받기
# 원자의 크기 N / 원자의 개수 M / 실험시간 t
N, M, t = map(int, input().split())
lst = []

for _ in range(M):
    x, y, m, s, d = map(int, input().split())
    lst.append([x, y, m, s, d, 1])  # 마지막: 원자 개수 카운트를 위해

# 8방향 리스트
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

## 시작
for T in range(t):
    # [1] 원자 이동하기
    for idx in range(len(lst)):
        if lst[idx] != []:
            d = lst[idx][4]  # 방향
            s = lst[idx][3]  # 속력
            nr, nc = (lst[idx][0] + s * di[d]) % N, (lst[idx][1] + s * dj[d]) % N

            lst[idx][0], lst[idx][1] = nr, nc

    # [2] 하나의 칸에 2개 이상의 원자가 있는 경우
    out_lst = []
    for idx in range(len(lst) - 1, -1, -1):
        x, y = lst[idx][0], lst[idx][1]
        # 좌표가 같은 원소들 하나로 합치기
        for nxt_idx in range(idx - 1, -1, -1):
            if x == lst[nxt_idx][0] and y == lst[nxt_idx][1]:
                out_lst.append(lst[nxt_idx])
                lst[idx][2], lst[idx][3] = lst[idx][2] + lst[nxt_idx][2], lst[idx][3] + lst[nxt_idx][3]
                lst[idx][5] += 1  # 같은 좌표 원자 개수

                # 방향처리
                if (lst[idx][4] % 2 == 0 and lst[nxt_idx][4] % 2 == 1) or \
                        (lst[idx][4] % 2 == 1 and lst[nxt_idx][4] % 2 == 0):
                    lst[idx][4] = 1
                else:
                    lst[idx][4] = 0

    # 합친 원자들은 이제 삭제
    lst = [mats for mats in lst if mats not in out_lst]

    # 합쳐진 원자 나누기
    for idx in range(len(lst)):
        x, y, m, s, d, cnt = lst.pop(0)
        for dir_num in range(4):
            if m // 5 != 0:  # 질량이 0이면 사라진다
                lst.append([x, y, m // 5, s // cnt, (d + dir_num * 2) % 8, 1])

# 질량 합 구하기
ans = 0
for wonza in lst:
    ans += wonza[2]
print(ans)
