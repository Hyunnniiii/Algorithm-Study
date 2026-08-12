
# 영양분별로 일정 수치 이상, 비용은 최소

def diet(idx, pro, fat, tan, vit, price, lst):
    global min_price, final_lst
    # 가지치기: 최소 비용 이미 넘겼을 때
    if price > min_price:
        return
    # 종료: 최소 합 조건 맞췄을 때 / 답이 없을 때 / 다 선택했을 때
    if idx == N:
        if pro >= mp and fat >= mf and tan >= ms and vit >= mv:
            if price < min_price:
                    min_price = price
                    final_lst = lst
            # 가격이 같다면 사전순으로 리스트 비교
            elif price == min_price and lst < final_lst:
                final_lst = lst
        return

    # 식재료 선택: 순열로 하면 시간 초과 나옴. 어차피 중복 안되니까 부분집합으로 처리하기
    diet(idx+1, pro, fat, tan, vit, price, lst)
    diet(idx+1, pro+arr[idx][0], fat+arr[idx][1], tan+arr[idx][2], vit+arr[idx][3], price+arr[idx][4], lst + [idx+1])   # 인덱스 1부터


N = int(input())
mp, mf, ms, mv = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

min_price = 500*N + 1
final_lst = []

diet(0,0,0,0,0,0,[])
if final_lst:
    print(min_price)
    print(*final_lst)
else:
    print(-1)
