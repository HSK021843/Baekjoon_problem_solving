lst = list(map(int, input().split()))
lst.sort()

if lst[2] < lst[0] + lst[1]:
    print(sum(lst))
else:
    print(2 * (lst[0] + lst[1]) - 1)