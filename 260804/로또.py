# K개 숫자들 중에서 6개만 선택해서 가능한 조합의 수
# 같은 숫자 중복 불가

lst = list(map(int, input().split()))
K = lst[0]

def lotto(n, start, lotto_num):
    # 종료조건: K개 골랐을 때
    if n == 6:
        print(*lotto_num)
        return

    # 번호 고르기
    for i in range(start, K+1):
        lotto(n+1, i+1, lotto_num + [lst[i]])

lotto(0,1,[])

