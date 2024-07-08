""" 

goal: 
      items should be deleted by parity odd/even or even/odd
      when deletion is impossible print the minimized sum
      input n int, a ints

strategy:
    when odds and evens are equal res is 0, 
    whenever odd > even -> minimize odd and vice versa
    case1
    [6,4,2]
    [5,3,1]
    3
    3
    min 3
    0
    case2
    [6,4,2 8 8]
    [5,3,1]
    min 3
    min

 """
def parity():
    n = int(input())
    a = list(map(int, input().split()))
    odd, even = [], []
    a = sorted(a, reverse=True)
    for i in a:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    e_a, o_a = len(even), len(odd)
    min_sum = min(e_a, o_a)
    if n == 1:
        print(0)
    elif min_sum == 0:
       print(sum(a[1:]))
    elif e_a == min_sum:
       print(sum(odd[min_sum+1:]))
    elif o_a == min_sum:
       print(sum(even[min_sum+1:]))

        
parity()
