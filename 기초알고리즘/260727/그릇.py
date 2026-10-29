lst = list(input())

height = 10
for x in range(len(lst)-1):
    # 같으면 +5
    if lst[x] == lst[x+1]:
        height += 5
    # 다르면 +10
    else:
        height += 10
print(height)