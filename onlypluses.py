""" 
understanding:

A B C, A or B or C +1
1 operation [5]
-> A x B x C 
i want to maximaze the product so
I have to make the integers as close to each other as possible 


input 
1 <= t <= ..
1 <= a b c <= 10

strategy
sort ascending 
add 1
this will keep the consisten equality between the numbers


1 1 1
+1
2 1 1
+1
2 2 1
+1
2 2 2
+1
3 2 2
+1
3 3 2



evaluation:
I didnt understand the output values and confused them with input restrictions
"""
t = int(input())
for _ in range(t):
    xyz = list(map(int, input().split()))
    for _ in range(5):
        xyz.sort()
        xyz[0] += 1
    print(xyz[0] * xyz[1] * xyz[2])
            

        


