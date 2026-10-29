# 모든 경우 > 백트래킹?
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [0]*(n+1)   # 골랐음을 표시하는 배열

# n/2개 고르는 함수
def choose_1(mlst, idx):
    global min_diff, morning, night
    nlst = []
    # 종료: n/2개 골랐을 때
    if len(mlst) == n//2:
        # 저녁도 구해야 하므로 저녁 리스트 만들기
        for x in range(1, n+1):
            if x not in mlst:
                nlst.append(x)

        # 여기에서 그 다음 작업 수행
        choose_2_morning(0, mlst, [], 0)
        choose_2_night(0, nlst, [], 0)

        min_diff = min(min_diff, abs(morning - night))
        return
    # 고르기
    for num1 in range(idx, n+1):
        if visit[num1] == 0:
            visit[num1] = 1
            choose_1(mlst + [num1], num1+1)
            visit[num1] = 0


# n/2개 고른 조합에서 또 조합을 만드는 함수
def choose_2_morning(cnt, lst, morninglst, idx):
    global morning
    if cnt == 0:
        morning = 0
    # 종료: 모든 조합 완료
    if cnt == 2:
        morning += arr[morninglst[0]-1][morninglst[1]-1]
        morning += arr[morninglst[1]-1][morninglst[0]-1]
        return
    # 고르기
    for num2 in range(idx, len(lst)):
        choose_2_morning(cnt+1, lst, morninglst + [lst[num2]], num2+1)

def choose_2_night(cnt, lst, nightlst, idx):
    global night
    if cnt == 0:
        night = 0
    # 종료: 모든 조합 완료
    if cnt == 2:
        night += arr[nightlst[0]-1][nightlst[1]-1]
        night += arr[nightlst[1]-1][nightlst[0]-1]
        return
    # 고르기
    for num2 in range(idx, len(lst)):
        choose_2_night(cnt+1, lst, nightlst + [lst[num2]], num2+1)

min_diff = float('inf')
a = choose_1([], 1)
print(min_diff)