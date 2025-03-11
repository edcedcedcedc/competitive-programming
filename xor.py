""" ]


 """








for i in range(int(input())):
    x = int(input())
    for y in range(1,x + 1): 
        if x + y > x^y:
            print(y, 'res')
            break
        elif y == x - 1:
            print(-1, 'res')
        
       