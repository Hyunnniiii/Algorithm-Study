# 정해진 칼로리 이하면서, 가장 점수가 높은 햄버거 조합
# 같은 재료 여러번 사용 불가
# 재료의 개수는 정해져 있지 않음 -> 부분조합

def burger(idx, taste, cal):
    global max_grade
    # 가지치기: 제한 칼로리 초과했을 때
    if cal > L:
        return
    # 종료 조건: 모두 선택했을 때
    if idx == N:
        if taste > max_grade:
            max_grade = taste
        return
    # 재료 선택하기
    burger(idx+1, taste + arr[idx][0], cal + arr[idx][1]) # 선택했을 때
    burger(idx+1, taste, cal)  # 선택 안했을 때


for T in range(1, int(input())+1):
    N, L = map(int, input().split())    # N: 재료의 수, L: 제한 칼로리
    arr = [list(map(int, input().split())) for _ in range(N)]   # 점수, 칼로리 표

    max_grade = 0
    burger(0, 0, 0)
    print(f'#{T} {max_grade}')