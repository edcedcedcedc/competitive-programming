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


#goal 
#asks q queries, for each query output the sum of all elements in
#the subarray of b that starts from the l-th element and ends at the r-th element inclusive 

#input
#t - test cases 
#n q - length arr and queries 
#n integers a1,a2,a3,an
#q lines of boundries l and r 

#strategy
#duplication - duplicate the n to get 2n, this is for all possible shifts
#findint the rotation - 
    #which rotation x corresponds to
    # (x - 1)/n + 1 ; 1 <= x <= n
    #which position whitin that rotation x corresponds to 
    #pos_x = (x - 1) mod n + 1  
#summation with prefix sums; the idea is to preprocess the array to maky summing more efficient
    #yi = yi-1 + xi
#conditionals
    #rl == rr then 
        #prefixsum[rl] - prefixsum[ll - 1]


t = int(input())  # Read number of test cases
for _ in range(t):
    n, q = map(int, input().split())  # Read n and q
    a = list(map(int, input().split()))  # Read array a
    a2 = a + a
    ps = [0]  # Initialize the prefix sum array
        
    # Compute prefix sums for the original array
    for val in a2:
        ps.append(ps[-1] + val)
    # l1    lr1    r
    #[0, 1, 3, 6, 7, 9, 12] prefix sums 
    #[1, 2, 3, 1, 2, 3] init array
    #example 2
    #3,4 -> 2,3 -> rotation 0, rotation 1 ->position 2, position 0 -> prefixsum(rotation + position) - prefixsum(rotation) -> right difference 3 -> prefixsum(rotation + n) - prefixsum(rotation)
    
    for _ in range(q):
        l, r = map(int, input().split())  # Read l and r
        l -= 1  # Convert to 0-based index
        r -= 1  # Convert to 0-based index
            
        rl = l // n  # Determine rotation for l
        rr = r // n  # Determine rotation for r
        l %= n  # Position of l within its rotation
        r %= n  # Position of r within its rotation
            
        left_bound = (ps[rl + l] - ps[rl]) 
        right_bound = (ps[rr + n] - ps[rr + r + 1])
        end = ps[n] * (rr - rl + 1) 
    
        total_sum = end- left_bound- right_bound
        print(total_sum)
 




""" 
Sure! Let's break it down in plain words, avoiding the math symbols as much as possible.

### Understanding the Problem

You are dealing with an array that repeats itself (like a **cyclic array**), and you want to find the sum of elements between two indices `l` and `r`. Since the array repeats, you might be asked to compute the sum for indices that fall **across** the boundary of a cycle. This is where things get a bit tricky, but we can handle it step by step.

### Key Concepts

1. **Cyclic Array**:  
   You can think of the array as a repeating sequence. For example, if your array is `[1, 2, 3]`, when it repeats, it becomes `[1, 2, 3, 1, 2, 3]`, and so on. It's like the array starts over after it reaches the end.

2. **Prefix Sum**:  
   A prefix sum is a running total of the array. It helps you quickly calculate the sum of any part of the array.  
   For example, if you have the array `[1, 2, 3, 4]`, the prefix sum would be `[0, 1, 3, 6, 10]`, where each number is the sum of the elements up to that point:
   - The first element is 0 (no sum yet).
   - The second element is 1 (the sum of the first element: `1`).
   - The third element is 3 (the sum of the first two elements: `1 + 2`).
   - The fourth element is 6 (the sum of the first three elements: `1 + 2 + 3`).
   - The fifth element is 10 (the sum of all elements: `1 + 2 + 3 + 4`).

3. **Cyclic Prefix Sum**:  
   When the array repeats, you extend the prefix sum to cover the whole repeated array. For example, if your array is `[1, 2, 3]` and you duplicate it (to handle the cyclic nature), you get:
   ```
   [1, 2, 3, 1, 2, 3]  (the repeated array)
   ```
   The prefix sum would be extended as well:
   ```
   [0, 1, 3, 6, 7, 9, 12]
   ```
   This helps in handling the cyclic nature because it gives you the cumulative sum for each position in the repeated array.

### Calculating the Sum for a Range

Now, let's focus on how you calculate the sum between two indices `l` and `r`.

1. **Dividing into Two Parts**:  
   If the indices `l` and `r` fall within the **same cycle**, you can simply use the prefix sum to get the sum of elements between `l` and `r`.  
   But if `l` and `r` fall across **two different cycles**, you need to split the sum calculation into two parts:
   - One part is the sum of elements from `l` to the end of the first cycle.
   - The other part is the sum of elements from the start of the second cycle to `r`.

2. **Left Part of the Sum**:  
   If `l` is within the first cycle, you need to calculate the sum from `l` to the end of the first cycle. To do this, you look at the prefix sum at `l`, subtract the prefix sum at the start of the cycle, and you get the sum of the elements starting at `l` and extending to the end of the first cycle.

3. **Right Part of the Sum**:  
   If `r` is within the second cycle (and `l` is in the first cycle), you need to calculate the sum from the start of the second cycle to `r`. Again, you use the prefix sum to get the cumulative sum at `r`, subtract the sum of elements up to the end of the first cycle, and you get the sum of elements in the second cycle.

4. **Full Cycle Consideration**:  
   If `l` and `r` span two cycles, the total sum between them involves:
   - Calculating the sum of elements in the first cycle up to `l`.
   - Adding the sum of elements in the second cycle up to `r`.
   - And finally, accounting for the **full cycles** in between (if any).

### Example Walkthrough (Non-Mathematical)

Let's say the array is `[1, 2, 3]`, and we have it duplicated to simulate the cyclic behavior:  
```
a2 = [1, 2, 3, 1, 2, 3]
```
Now, suppose we want to find the sum of elements from index `2` to index `5` (1-based indices).

1. **Convert to 0-based Indices**:  
   We convert `l = 2` and `r = 5` to 0-based indices:
   - `l = 2 - 1 = 1`
   - `r = 5 - 1 = 4`

2. **Calculate Rotations**:
   - The first rotation (or cycle) is from index `0` to `2`.
   - The second rotation (or cycle) is from index `3` to `5`.

   In this case, `l = 1` is in the **first cycle**, and `r = 4` is in the **second cycle**.

3. **Split the Calculation**:
   We need to split the sum into two parts:
   - The **left part** is the sum from index `1` (which is `2` in the original array) to the end of the first cycle. The sum in the first cycle is from `a[1]` to `a[2]`, which is `2 + 3 = 5`.
   - The **right part** is the sum from the start of the second cycle to index `4`. The sum in the second cycle is from `a[3]` (which is `1` in the original array) to `a[4]`, which is `1 + 2 = 3`.

4. **Final Sum**:
   The total sum is the sum of the two parts:
   - Left part = `5`
   - Right part = `3`
   - Total sum = `5 + 3 = 8`

This is how the program splits the range into two parts and calculates the sum for each part using the prefix sum array.

### Summary:
- If your query range (`l` to `r`) falls within a **single rotation**, the sum is straightforward, and you can directly use the prefix sum.
- If the query range spans **two rotations**, you split the sum calculation into two parts:
  - One part for the first cycle, and
  - One part for the second cycle.
- By using the prefix sum, the program efficiently computes the sum without having to iterate over all elements between `l` and `r`.




 """
        
    