
""" 조삼모사 / 20260917 / 체감 난이도: 실버
소요 시간 20분 / 시도 1회 / 실행 시간 933ms (코드트리) / 메모리 24MB (코드트리)

진심 나 옛날에 뭐한거임? N/2개를 골라서 그 중에서 또 조합을 만든다??가 뭐하는거지??
과거의 나의 로직이 이해가 안됨.
아무튼 백트래킹 필수 루틴: 시복 계산, 2^50 넘으면 시도 X, 순열/조합 판별
..라고 생각했으나, 이게 결국 아침 <-> 저녁 똑같은데 낮밤만 바뀐 경우 결국 중복이 발생한다.
그거에 대한 처리를, 한쪽에만 0 넣어주면 되는건데 (스터디때 종협이 그렇게 했던 것도 문제 풀고 933 떠서 기억남)
아무튼 백트래킹 연습 겸 풀어봄

"""

# N개의 일이 주어졌을 때, 절반씩 나눠서 아침/저녁에 처리
# 구할 것: 아침과 저녁의 업무 강도의 차이의 최솟값

# 일단 완탐임 > N개에 대해 할지 말지 정함 > 최대 2^20 > 백트래킹 ok
# 아침에 할 일만 딱 구하면 저녁은 알아서 정해진다
# 순열 아니고 조합임. 중복 연산 안되게 처리
# ===================
import sys
sys.stdin = open('input.txt', 'r')


def btrk(idx, cnt, morning):
    global min_gap

    # 종료: N/2개 다 정하면 끝
    if cnt == N//2:
        night = []
        for x in range(N):
            if x not in morning:
                night.append(x)

        m, n = 0, 0     # 낮, 밤의 일의 합
        for x in morning:
            for y in morning:
                if y == x:
                    continue
                m += arr[x][y]

        for x in night:
            for y in night:
                if y==x:
                    continue
                n += arr[x][y]

        min_gap = min(abs(m-n), min_gap)
        return

    # 종료: N개에 대해 선택했으나 정확히 절반을 고르진 않음 > no 정산
    if idx == N:
        return

    # 실행: 아침에 이 일 할래말래
    btrk(idx+1, cnt+1, morning+[idx])
    btrk(idx+1, cnt, morning)


##########################
N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]

min_gap = float('inf')
btrk(0,0,[])
print(min_gap)