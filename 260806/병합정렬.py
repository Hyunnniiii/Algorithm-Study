for T in range(1, int(input())+1):
    N = int(input())
    L = list(map(int, input().split()))

    cnt = 0

    def merge(lst):
        global cnt
        # 종료: 쪼갠 길이가 1보다 작아질 때까지
        if len(lst) <= 1:
            return lst
        # 쪼개기 수행
        K = len(lst) // 2
        left = merge(lst[:K])
        right = merge(lst[K:])

        # 다 쪼개진 애들 병합하는 작업
        res = []
        index1, index2 = 0, 0
        findex1, findex2 = len(left), len(right)

        # 병합하기 전에 마지막 숫자 대소 비교
        if left[findex1-1] > right[findex2-1]:
            cnt += 1

        # 병합하기
        # 인덱스 범위 내에서 비교하는 동안
        while index1 < findex1 and index2 < findex2:
            if left[index1] > right[index2]:
                res.append(right[index2])
                index2 += 1
            else:
                res.append(left[index1])
                index1 += 1

        # 범위 넘어가면 남은 숫자 전체 붙여넣기
        if index1 >= findex1:
            res.extend(right[index2:])
        elif index2 >= findex2:
            res.extend(left[index1:])

        return res

    result = merge(L)
    print(f'#{T} {result[N//2]} {cnt}')


