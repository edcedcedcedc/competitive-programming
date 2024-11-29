import math

#arithmetic series

#k,k+1,k+2,k+3..k+n-1
#1,2,3,4          a_i = a + (i - 1)d
#1+2+3+4          S_n = 2*k+(n - 1)d/2 or n(n + 1)/2
#1^2+2^2+3^2      S_n = n(n + 1)(2n + 1)/6

#geometric series

#a,ak,ak^2,ak^3,ak^n-1
#3,6,12,24         a_n = a * r^n-1  r-common ratio n-position of the term
#3+6+12+24         b*k - a/k - 1    a-first number b-last number k-common ratio  S = a + ak + ak^2 + · · · + b
#1+2+4+8+16+2^n-1  2^k-1 - special case

#fibonacci
#f(n-1)+f(n-2)

#factorial
#n*f(n-1)
#math.factorial()

#minimum
#minimum = float('inf')
#if a < minimum:
#    minimum = a

#maximum
#maximum = float('-inf')
#if a < maximum:
#    maximum = a

#sets                                                                                            
#The intersection A ∩ B -> A and B
#example, if A = {1, 2, 5} and B = {2, 4}, then A ∩ B = {2}.


#The union A ∪ B -> A or B or BOTH
#example, if A = {3, 7} and B = {2, 3, 8}, then A ∪ B = {2, 3, 7, 8}


#first_set(.intersection.union.difference.symmetric_difference)(second_set)

#symmetric difference - or A or B but not A and B


#log 
#log_k(x) - k/x till 1 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1
#log_k(ab) = log_k(a) + log_k(b)
#log_k(xn) = n · log_k(x)


#bisection
#lo,hi,mid,while lo hi, condition, lo/hi mid + 1/mid - 1



#understanding:
#1)goal,what I know, what I dont know, 
#2)observation/breakdown/induce/deduce
#3)loops/statements/varibles
#3.1)how to start/ how in the middle, how to end
#strategy
#implimentation
#evaluation

# ______ _    _ _____   ____  _____   ____  _      _               _____   _____ _     _    _ ____  
# |  ____| |  | |  __ \ / __ \|  __ \ / __ \| |    | |        /\   |  __ \ / ____| |   | |  | |  _ \ 
# | |__  | |  | | |__) | |  | | |  | | |  | | |    | |       /  \  | |__) | |    | |   | |  | | |_) |
# |  __| | |  | |  _  /| |  | | |  | | |  | | |    | |      / /\ \ |  _  /| |    | |   | |  | |  _ < 
# | |____| |__| | | \ \| |__| | |__| | |__| | |____| |____ / ____ \| | \ \| |____| |___| |__| | |_) |
# |______|\____/|_|  \_\\____/|_____/ \____/|______|______/_/    \_\_|  \_\\_____|______\____/|____/ 



""" 
k - showel price 
r - 1 <= r <= 9 
t - unlimited 10
i - 1 <= i <= inf


117 - k, r = 3, i - ?

117 * 1 = 117
117 * 2 = 234
117 * 3 = 351
117 * 4 = 468
117 * 5 = 585
117 * 6 = 702
117 * 7 = 819
117 * 8 = 936
117 * 9 = 1053 case 2 117 * x = y
117 * 10 = 1070 case 3
117 * 11 = 1287

117 * x = y - r

117 * x mod 10 = r




113 7 = 9

237 7 = 1

15 2 = 2



 """


k, r = map(int, input().split()); i = 1
while 0 != k * i % 10 != r: 
    i += 1
print(i)


