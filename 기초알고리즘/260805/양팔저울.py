# min: 가장 작은 값, max: 모두 더한 값
# 선택하는 것 뿐만 아니라 값을 뺄 수도 있다
# 1부터 S 사이 못 만드는 정수 구하기

k = int(input())    # k: 추의 개수
lst = list(map(int, input().split()))   # 추의 무게 리스트
S = sum(lst)    # 모든 추의 무게 합
num_set = set()

def dfs(idx, sm):
    # 종료: k개에 대해 모두 결정 완료
    if idx == k:
        if sm >= 1 and sm not in num_set:
            num_set.add(sm)
        return
    # 숫자 고르기: 더하거나, 빼거나, 안하거나
    dfs(idx+1, sm)
    dfs(idx+1, sm + lst[idx])
    dfs(idx+1, sm - lst[idx])

dfs(0,0)
print(S-len(num_set))