import math
quantity_of_groups = int(input())
groups = list(map(int, input().split()))
taxis_needed = 0
if 1 in groups:
    taxis_needed = sum(filter(lambda x: x == 3, groups))/3
    taxis_needed_by_1 = sum(filter(lambda x: x == 1, groups))/4
    taxis_left_from_3 = len(list(filter(lambda x: x == 3, groups)))/4
    if taxis_needed_by_1 > taxis_left_from_3:
        taxis_needed += sum(filter(lambda x: x != 3 and x != 1, groups))/4 + (taxis_needed_by_1 - taxis_left_from_3)
    else:
        taxis_needed += sum(filter(lambda x: x != 3 and x != 1, groups))/4
   
       
else: 
    taxis_needed = sum(filter(lambda x: x == 3, groups))/3 + sum(filter(lambda x: x != 3, groups))/4
    
print(math.ceil(taxis_needed))

""" from math import ceil
n=int(input())
s=list(map(int,input().split()))
a=s.count(4) #count_items of the same value
b=s.count(3)
c=s.count(2)
d=s.count(1)
p=a+b #taxi_needed 
print(a,b,c,d) 
if d<=b:# count of d less or equal to b 
    p=p+ceil(c/2)#
else :
    p=p+ceil((d-b+2*c)/4)
print(p) 
 """
