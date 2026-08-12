for T in range(1, int(input())+1):
    N = int(input())
    nums = list(map(int, input().split()))

    # 단순정렬
    for x in range(N-1):
        for y in range(x+1, N):
            if nums[x] > nums[y]:
                nums[x], nums[y] = nums[y], nums[x]

    print(f'#{T} {nums[N//2]}')

    # 퀵정렬
    def quick(lst):
        # 종료: 나눌게 없을 때-리스트 안에 0개 또는 1개
        if len(lst) <= 1:
            return lst
        # 단위행동: pivot 기준으로 좌우 나눈 다음에 좌+pivot+우
        pivot = lst[0]
        left = []
        right = []
        for x in lst[1:]:
            if pivot > x:
                left.append(x)
            else:
                right.append(x)
        return quick(left) + [pivot] + quick(right)

    sorted_lst = quick(nums)
    print(f'#{T} {sorted_lst[N//2]}')

    # 병합정렬
    def merge(lst):
        # 1개 될 때까지 다 쪼개기
        if len(lst) == 1:
            return lst

        # 절반씩 나누기, 재귀
        K = len(lst)
        mid = K // 2
        left = merge(lst[ : mid])
        right = merge(lst[mid : ])

        # 다 나눈 것들 순서대로 합치기
        res = []    # 정렬한 결과 넣을 리스트
        index1 = index2 = 0     # 좌/우 인덱스
        # 1. 인덱스 범위 내에서 비교할 때
        while index1 < len(left) and index2 < len(right):
            # 대소비교해서 추가
            if left[index1] > right[index2]:
                res.append(right[index2])
                index2 += 1
            else:
                res.append(left[index1])
                index1 += 1

        # 2. 인덱스 범위 벗어났을 때
        if index1 >= len(left):  # 왼쪽에서 먼저 끝난 경우
            res.extend(right[index2: ])
        elif index2 >= len(right):   # 오른쪽 먼저 끝난 경우
            res.extend(left[index1: ])

        # 결과 확인
        return res

    result = merge(nums)
    print(result)



    # sort 정렬
    nums.sort()
    print(nums)