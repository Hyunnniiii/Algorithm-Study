# 입력받은 숫자보다 큰 수가 뒤에 있으면 이득 > max 값 기준으로 생각하기
for T in range(1, int(input())+1):
    N = int(input())

    lst = list(map(int, input().split()))
    income = 0

    while lst:
        max_price = max(lst)
        max_idx = lst.index(max_price)

        # 최고 가격이 될 때까지 이익 계산
        for cost in lst[:max_idx]:
            income += max_price - cost

        # 최고 가격까지의 이익을 모두 계산하면 기존 리스트 삭제
        del lst[:max_idx + 1]

    print(f'#{T} {income}')

# 문제에서 조건: 2 <= N <= 1,000,000 -> 시간 복잡도 고려해야 한다 (10^8 기준)
# 아래와 같이 루프마다 max값을 구한다면 시간 초과가 날 수 있다.. 생각을 좀 더 해봐야 함

    # for i in range(N - 1):
    #     target = max(price[i + 1:])
    #
    #     if price[i] < target:
    #         ans += target - price[i]
    #
    # print(f"#{tc} {ans}")

# 뒤에서부터 비교하면 더 효율적이다
# -1 인덱스를 max로 잡은 다음에 앞으로 루프 돌린다.
# # max보다 큰 값이 나타나면 max 갱신, 그 전까지 수익 계산

# 개선한 코드
for T in range(1, int(input())+1):
    N = int(input())

    lst = list(map(int, input().split()))
    income = 0
    max_price = lst[-1]
    for x in range(N-2, -1, -1):
        # 뒤에서부터 최고 가격이 바뀔 때까지 이익 계산
        if max_price < lst[x]:
            max_price = lst[x]
        else:
            income += max_price - lst[x]
    print(f'#{T} {income}')
