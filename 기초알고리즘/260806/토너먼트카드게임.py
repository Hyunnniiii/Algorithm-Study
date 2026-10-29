# 1 가위 / 2 바위 / 3 보

for T in range(1, int(input())+1):
    N = int(input())
    cards = list(map(int, input().split()))
    game = [[i+1, cards[i]] for i in range(N)]    # 학생 번호와 카드 숫자 함께 저장

    # 그룹 나누기
    def merge(lst):
        # 1명이 되면 끝
        if len(lst) <= 1:
            return lst[0]
        # 팀 나누기
        K = len(lst)
        mid = (K+1)//2
        left = merge(lst[:mid])
        right = merge(lst[mid:])

        left_num, left_card = left
        right_num, right_card = right

        # 가위바위보
        # 비겼을 때
        if left_card == right_card:
            return left
        # 가위/보 일때
        elif left_card == 1 and right_card == 3:
            return left
        elif left_card == 3 and right_card == 1:
            return right
        # 나머지
        elif left_card < right_card:
            return right
        elif left_card > right_card:
            return left

    winner = merge(game)
    print(f'#{T} {winner[0]}')


