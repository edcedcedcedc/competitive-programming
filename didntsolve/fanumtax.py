for i in range(int(input())):
    n, m = list(map(int, input().split()))
    a = list(map(lambda x: {"v": int(x), "c": False}, input().split()))
    b = int(input())
    if len(a) == 1:
        print("YES")
    else:
        pass