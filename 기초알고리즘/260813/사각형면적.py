# 세로로 자를 때: 가로 길이 비교해서 큰 쪽
# 가로로 자를 때: 세로 길이 비교해서 큰 쪽
# 위에서 선택한 2개 중 큰거 선택, 같으면 가로

# N: 초기 길이 / C: 자르는 점 개수
N, C = map(int, input().split())
garo, sero = N, N

for _ in range(C):
    cur_x, cur_y = map(int, input().split())

    if 0 <= cur_x < sero and 0 <= cur_y < garo:

        # 세로로 자른다면
        s_area = cur_y * sero

        # 가로로 자른다면
        g_area = cur_x * garo

        max_area = max(s_area, g_area)

        # 가로 우선
        if max_area == g_area:
            sero = cur_x
        elif max_area == s_area:
            garo = cur_y

print(garo * sero)