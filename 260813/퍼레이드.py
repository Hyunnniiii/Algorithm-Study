D = int(input())
cur = [0,0]     # 현재 위치한 좌표
ilst = set()    # 방문했던 수직방향 도로
jlst = set()    # 방문했던 수평방향 도로

# 방향에 따른 좌표 계산 함수
def move(dir, length):
    # 북쪽 방향
    if dir == 'N':
        cur[1] += length
    # 남쪽 방향
    if dir == 'S':
        cur[1] -= length
    # 동쪽 방향
    if dir == 'E':
        cur[0] += length
    # 서쪽 방향
    if dir == 'W':
        cur[0] -= length

# 시작
for _ in range(D):
    dir, length = map(str, input().split())
    length = int(length)

    move(dir, length)

    # 동서 방향으로 움직였으면 가로방향 도로
    if dir == 'E' or dir == 'W':
        ilst.add(cur[1])
    # 남북 방향으로 움직였으면 세로방향 도로
    if dir == 'S' or dir == 'N':
        jlst.add(cur[0])

# 가로 세로 도로 개수 세기
a, b = len(ilst), len(jlst)
print(a+b)
