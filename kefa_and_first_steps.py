t = int(input())
a = list(map(int, input().split()))
mx = 0
curr = 0
for j in range(len(a)):
    if len(a) - 1 == j:
        if a[j - 1] <= a[j]:
            curr += 1
        mx = max(curr, mx)
    elif a[j] <= a[j + 1]:
        curr += 1
    else:
        curr += 1
        mx = max(curr, mx)
        curr = 0

print(mx)
