

""" 연산자 배치하기 / 20261001 배고프고 졸리다 / 체감 난이도: 브론즈
소요 시간 약 10분 / 시도 1회 / 실행 시간 91ms (코드트리) / 메모리 19MB (코드트리)

그냥 백트래킹 연습 겸 풀어봄

"""

def btrk(select, res):
    global min_res, max_res
    # 종료: N-1개 선택 완료
    if select == N-1:
        min_res = min(min_res, res)
        max_res = max(max_res, res)
        return
    # 실행: 개수 남아있는 연산자 중 하나 선택해서 연산 수행
    for k in range(3):
        if cnt[k] == 0:
            continue
        cnt[k] -= 1
        if k==0:    # 더하기
            btrk(select+1, res+nums[select+1])

        elif k==1:  # 빼기
            btrk(select+1, res-nums[select+1])
        elif k==2:  # 곱하기
            btrk(select+1, res*nums[select+1])
        cnt[k] += 1

N = int(input().strip())
nums = list(map(int, input().split()))
cnt = list(map(int, input().split()))

min_res, max_res = float('inf'), -float('inf')
btrk(0,nums[0])
print(min_res, max_res)