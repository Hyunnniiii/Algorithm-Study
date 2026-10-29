# 배열 생성하고 해당하는 좌표에 몇 번째 번호인지 그 번호 추가
# 다음 색종이 받았을 때 겹치는 인덱스 부분에서 해당 색종이 번호 빼기
# 그러면서 새로운 색종이의 좌표에 번호 추가

N = int(input())
arr = [[0]*1001 for _ in range(1001)]

for i in range(1, N+1):
    start_x, start_y, row_length, col_length = map(int, input().split())
    end_x = start_x + row_length
    end_y = start_y + col_length

    # 색종이에 해당하는 영역에 번호 표시
    # 색종이가 겹치면 새로운 색종이의 번호로 다시 표시한다
    for r in range(start_x, end_x):
        for c in range(start_y, end_y):
            arr[r][c] = i

# 생성된 배열에서 색종이 번호별로 개수 카운트
num_count = [0] * N
for rows in arr:
    for nums in rows:
        if nums != 0:
            num_count[nums - 1] += 1

for x in num_count:
    print(x)