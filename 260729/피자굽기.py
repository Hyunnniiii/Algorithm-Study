# N개 화덕 / M개 피자 / Ci 치즈. 3<=N<=20, N<=M<=100, 1<=Ci<=20
# 화덕 1바퀴 -> 치즈 양 절반
# 치즈 0이 되면 화덕에서 꺼내고 그 자리에 남은 피자

for T in range(1, int(input())+1):
    N, M = map(int, input().split())    # N: 화덕, M: 피자

    pizza = [[] for _ in range(M)]      # 피자 큐
    p = list(map(int, input().split()))
    for i in range(M):
        pizza[i] = (i+1, p[i])

    # 또는 아래와 같이 생성 가능
    # for idx, pizza in enumerate(p):
        # pizza.append([idx+1, pizza])

    fire = []  # 화덕 큐
    for _ in range(N):
        fire.append(pizza[0])
        pizza.pop(0)

    # 화덕 돌리기
    while len(fire) > 1:
        num, cheese = fire.pop(0)
        cheese //= 2

        if cheese != 0:
            fire.append((num, cheese))
        else:
            # 남은 피자가 있을 때
            if pizza:
                new = pizza.pop(0)
                fire.append(new)

    print(f'#{T}', fire[0][0])











    # fire = []   # 화덕
    # for i in range(N):
    #     fire.append([i+1, pizza[i]])
    #
    # cur_pizza =    # 현재까지 넣은 피자의 수
    #
    # # 화덕에 피자가 1개 남을 때까지 반복
    # while len(fire) > 1:
    #     num, cheese = fire.pop(0)
    #     cheese //= 2
    #
    #     # 남은 치즈가 0이면 pop, 새로운 피자 넣는다
    #     if cheese == 0:
    #         if cur_pizza < M:
    #             fire.append([cur_pizza+1, pizza[cur_pizza]])
    #             cur_pizza += 1
    #
    #     else:
    #         fire.append([num, cheese])








