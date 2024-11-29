#arithmetic_sum = (2*k + n - 1) * n //2

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    low = 1
    high = n
    mini = float('inf')
    while low <= high:
        mid = (low + high) // 2
        sum1 = mid * (2 * k + (mid - 1)) // 2
        sum2 = n * (2 * k + (n - 1)) // 2 - sum1
        if sum1 < sum2:
            low = mid + 1
        else:
            high = mid - 1
        diff = abs(sum1 - sum2)
        if diff < mini:
            mini = diff    
    print(mini)
        