# 처음엔 하루에 7갤런
# 측정이 날짜 순으로 기록되지 않음
# 가장 많은 우유를 생산하는 소의 사진을 걸어둠. 동점이면 모두
# 구할 것: 사진을 변경해야 하는 날의 수

N = int(input().strip())
milk = [7, 7, 7]     # Bessie, Elsie, Mildred

# 입력 받고 날짜 순으로 정렬
history = [list(map(str, input().split())) for _ in range(N)]
history.sort(key = lambda x : int(x[0]))

# 우유 양 바꾸는 함수
# name에 따라 지정된 인덱스의 우유 생산량을 변경한다
def changemilk(name, change):
    if name == 'Bessie':
        milk[0] += change
    elif name == 'Elsie':
        milk[1] += change
    elif name == 'Mildred':
        milk[2] += change

# 날짜 순으로 하나씩 꺼내서 milk 양 수정
cnt = 0     # 바뀌는 횟수
pre_idx = [0, 1, 2]    # 액자에 걸리는 소의 인덱스 저장
pro_idx = []
for x in history:
    date, name, change = x[0], x[1], x[2]
    date, change = int(date), int(change)

    # 우유 생산량 변화 반영하기
    changemilk(name, change)

    # 바뀐 뒤의 최대 인덱스 확인
    max_milk = max(milk)
    for i in range(3):
        if milk[i] == max_milk:
            pro_idx.append(i)

    # 바뀌었다면 액자 변경
    if pre_idx != pro_idx:
        cnt += 1

    pre_idx = pro_idx   # 다음 비교를 위해
    pro_idx = []

print(cnt)

# ==========================

# 딕셔너리로 풀어보기
N = int(input().strip())
milk = {'Bessie': 7, 'Elsie': 7, 'Mildred': 7}

# 입력 받고 날짜 순으로 정렬
history = [list(map(str, input().split())) for _ in range(N)]
history.sort(key = lambda x : int(x[0]))


pre = {'Bessie', 'Elsie', 'Mildred'}
cnt = 0

for date, name, change in history:
    date, change = int(date), int(change)

    # 우유 생산량 변화 반영하기
    milk[name] += change

    # 바뀐 뒤의 최대 인덱스 확인
    max_milk = max(milk.values())

    # 현재 사진에 걸릴 소 담을 집합
    cur = set()

    for cow, amount in milk.items():
        if amount == max_milk:
            cur.add(cow)

    # 바뀌었다면 액자 변경
    if pre != cur:
        cnt += 1

    pre = cur

print(cnt)