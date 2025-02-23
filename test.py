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


""" 
input t
a line of integers a and b

m must be greater than or at least equal to a or b
remainder when m is divided by a must be equalt to te remainder when m is divided by b


m > a or m > b
m mod a >= m mod b

find the smallest integer m that satisfy the condition 


read mode on lcm, gcd


24 16

gcd(24,16) = 8
24/8 16/8
lca = |a * b| / gcd(24,6) = 48

 """


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(abs(a * b) // math.gcd(a,b))

""" t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    m = max(a,b)
    while (m % a != m % b):
        m += 1
    print(m)
 """