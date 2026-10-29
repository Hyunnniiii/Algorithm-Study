import random, time
MIN_VAL, MAX_VAL = 1, 99
numb = 100

start_time = time.time()

N = int(input().strip())
work = []
for _ in range(N):
    work.append(list(map(int, input().split())))

max_don = 0
def btrk(start, don):
    global max_don
    # 종료: N일까지에 대해 선택 완료
    if start >= N:
        max_don = max(max_don, don)
        return
    # 각 일자마다 일을 할지 말지 선택하기
    if start+work[start][0] <= N:
        btrk(start+work[start][0] , don + work[start][1])
        btrk(start+1, don)
    else:
        btrk(start + 1, don)
btrk(0,0)
print(max_don)

end_time = time.time()
print(f'{end_time - start_time:.10f}')