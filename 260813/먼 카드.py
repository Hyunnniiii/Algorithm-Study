# N=1일 때 답은 0
N = int(input())
cards = list(map(int, input().split()))
score = []

for idx in range(1, N+1):   # 찾는 숫자
    for k in range(2*N):   # 리스트 인덱스
        # 카드 리스트를 돌다가 해당 숫자가 나오면 카운트 시작
        if cards[k] == idx:
            cnt = 0

            for j in range(k+1, 2*N):
                # 같은 카드가 안나오면 +1
                if cards[j] != idx:
                    cnt += 1
                # 같은 카드 나오면 종료
                if cards[j] == idx:
                    break

            score.append(cnt)
            break

print(max(score))

