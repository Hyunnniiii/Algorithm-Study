# 가로 1000 이하
# 맨 왼쪽 두칸, 맨 오른쪽 두칸은 건물 안 짓는다
# 각 빌딩의 높이는 최대 255

for T in range(1, int(input())+1):
    N = int(input())

    # 건물 높이 리스트
    lst = list(map(int, input().split()))
    good_room = 0

    # 앞뒤로 거리 2인 건물들과 비교
    for x in range(2, N-2):
        peri_room = []
        # 조망권 있는 경우
        if lst[x] > lst[x-1] and lst[x] > lst[x-2] and lst[x] > lst[x+1] and lst[x] > lst[x+2]:
            for i in (-2,-1,1,2):
                peri_room.append(lst[x+i])

            max_peri = max(peri_room)
            good_room += lst[x] - max_peri
        # 조망권 없으면 패스
        else:
            continue

    print(f'#{T} {good_room}')


