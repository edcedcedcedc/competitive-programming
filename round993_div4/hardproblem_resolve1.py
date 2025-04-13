for _ in range(int(input())):
    m, a, b, c = list(map(int, input().split()))
    r = 0
    r += min(m, a)
    if m - a >= 1:
        r += min(c, m - a)
        c = c - min(c, m - a)
    r += min(m, b)
    if m - b >= 1:
        r += min(c, m - b)
    print(r)

    """ 
    example with positive m - a
    ---a
    ------m
       ---m - a
       ----c
    example with negative m - a
        ---a
        --m
       -m - a
        --c
    """
