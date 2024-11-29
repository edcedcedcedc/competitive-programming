import math

###################### CONTACT ME ####################### 
# EMAIL: ranogaet@gmail.com or TELEGRAM: @eurodollarclub
# For antispam write this in the title or first message: edc
#########################################################

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
#
#' /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#' \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
#' /\ _______ _    _ ______   _____         _____ _______   _____  _____       /\
#' \/|__   __| |  | |  ____| |  __ \ /\    / ____|__   __| |_   _|/ ____|      \/
#' /\   | |  | |__| | |__    | |__) /  \  | (___    | |      | | | (___        /\
#' \/   | |  |  __  |  __|   |  ___/ /\ \  \___ \   | |      | |  \___ \       \/
#' /\   | |  | |  | | |____  | |  / ____ \ ____) |  | |     _| |_ ____) |      /\
#' \/ __|_|__|_|  |_|______| |_| /_/    \_\_____/   |_|    |_____|_____/       \/
#' /\|__   __| |  | |  ____|                                                   /\
#' \/   | |  | |__| | |__                                                      \/
#' /\   | |  |  __  |  __|                                                     /\
#' \/   | |  | |  | | |____                                                    \/
#' /\ __|_|__|_|  |_|______|_____  _____ _______ _______     __   ____  ______ /\
#' \/|__   __|/\   |  __ \|  ____|/ ____|__   __|  __ \ \   / /  / __ \|  ____|\/
#' /\   | |  /  \  | |__) | |__  | (___    | |  | |__) \ \_/ /  | |  | | |__   /\
#' \/   | | / /\ \ |  ___/|  __|  \___ \   | |  |  _  / \   /   | |  | |  __|  \/
#' /\   | |/ ____ \| |    | |____ ____) |  | |  | | \ \  | |    | |__| | |     /\
#' \/__ |_/_/    \_\_|  _ |______|_____/  _|_|  |_|__\_\_|_|_  __\____/|_|     \/
#' /\\ \        / / |  | |   /\|__   __| | |    |_   _|  ____|/ ____|          /\
#' \/ \ \  /\  / /| |__| |  /  \  | |    | |      | | | |__  | (___            \/
#' /\  \ \/  \/ / |  __  | / /\ \ | |    | |      | | |  __|  \___ \           /\
#' \/   \  /\  /  | |  | |/ ____ \| |    | |____ _| |_| |____ ____) |          \/
#' /\    \/  \/_  |_| _|_/_/    \_\_| ___|______|_____|______|_____/           /\
#' \/    /\   | |  | |  ____|   /\   |  __ \                                   \/
#' /\   /  \  | |__| | |__     /  \  | |  | |                                  /\
#' \/  / /\ \ |  __  |  __|   / /\ \ | |  | |                                  \/
#' /\ / ____ \| |  | | |____ / ____ \| |__| |                                  /\
#' \//_/    \_\_|  |_|______/_/    \_\_____/                                   \/
#' /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#' \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

 
#strategy 1 ; WRONG
# if value(n) < 10 then value(n)
# elif index(n - 1) == index(n - 2) then count(digits(n - 1)) * 9 + index_value(n)
# elif n - 1 != n - 2 then count(digits(n - 1)) * 9 + index_value(n[0] - 1)

#strategy 2 ; WRONG
# if n < 10 then n
# elif n - i == n then count(digits(n - 1)) * 9 + n 
# elif n - i != n then count(digits(n - 1)) * 9 + n[0] - 1 if 0 then n[0] - 2
 

#some observations ; 
#1 1 1 1 1 1 1 1 1

#1 2 3 4 5 6 7 8 9 
#1 2 3 4 5 6 7 8 9

#  2  4  6  8 10 12 14 16 18

# 11 22 33 44 55 66 77 88 99 
# 10 11 12 13 14 15 16 17 18

#  3   6   9   12  15  18  21  24  27

# 111 222 333 444 555 666 777 888 999 
# 19  20  21  22  23  24  25  26  27

#  4    8    12   16   20   24   28   32   36

# 1111 2222 3333 4444 5555 6666 7777 8888 9999
# 28   29   30   31   32   33   34   35   36

#strategy 3: GOOD!
#strategy
#precompute ordinary for optimization 
#next ordinary is j * 10 + i


#strategy 4:
#main part 

#induction 

#9 = 9
#999 = 9 + 9 + 9 
#99 = 9 + 9
#9 * (len(n)-1) 

#counter part
#9
#9 + 0
#13
#9 + 13 // 11 = 10
# int(n) // int("1"*len(n))

""" def o():
    o = []
    for i in range(1,10):
        j = i
        while j <= 10**9:
            o.append(j)
            j = (j * 10) + i
    o.sort()
    return o

o = o()

t = int(input())
for _ in range(t):
    r = 0
    n = int(input())
    for j in o:
        if n < j:
            break
        r += 1
    print(r) """


for _ in range(int(input())):
    n = input()
    print(9 * (len(n) - 1) + int(n) // int("1" * len(n)))
 