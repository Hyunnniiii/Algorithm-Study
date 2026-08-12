# 트럭당 1개의 컨테이너. 적재용량 초과하면 운반할 수 없음.
# 이동한 화물의 총 용량이 최대가 되도록 했을 때 옮겨진 화물의 전체 무게?

for TC in range(1, int(input())+1):

    # N: 컨테이너 수 / M: 트럭 수
    N, M = map(int, input().split())

    # N개 화물의 무게
    w = list(map(int, input().split()))
    # M개 트럭의 적재용량
    t = list(map(int, input().split()))

    #  가장 큰 트럭부터 순차적으로 본인이 들 수 있는 가장 최대의 화물을 하나씩 고른다
    w.sort(reverse=True)
    t.sort(reverse=True)

    tot_weight = 0
    for i in range(M):
        for j in range(len(w)):
            # 적재 용량보다 작은게 등장하면 그걸 선택, 리스트에서 지우기
            if t[i] >= w[j]:
                tot_weight += w[j]
                w.remove(w[j])  # remove 말고 pop(j)를 하면 더 좋다
                break

    print(f'#{TC} {tot_weight}')