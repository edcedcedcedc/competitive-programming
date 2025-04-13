for i in range(int(input())):
    n, m, l, r = list(map(int, input().split()))
    d = n - m
    if d == 0:
        print(l, r)
    else:
        l_prime = l + d
        if l_prime > 0:
            r_prime = r - l_prime
            l_prime = 0
            print(l_prime, r_prime)
        else:
            print(l_prime, r)
