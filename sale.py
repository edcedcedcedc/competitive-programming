"""
B. Sale
time limit per test2 seconds
memory limit per test256 megabytes
Once Bob got to a sale of old TV sets. There were n TV sets at that sale. TV set with index i costs ai bellars. Some TV sets have a negative price — their owners are ready to pay Bob if he buys their useless apparatus. Bob can «buy» any TV sets he wants. Though he's very strong, Bob can carry at most m TV sets, and he has no desire to go to the sale for the second time. Please, help Bob find out the maximum sum of money that he can earn.

Input
The first line contains two space-separated integers n and m (1 ≤ m ≤ n ≤ 100) — amount of TV sets at the sale, and amount of TV sets that Bob can carry. The following line contains n space-separated integers ai ( - 1000 ≤ ai ≤ 1000) — prices of the TV sets.

Output
Output the only number — the maximum sum of money that Bob can earn, given that he can carry at most m TV sets.

Examples
InputCopy
5 3
-6 0 35 -2 4
OutputCopy
8
InputCopy
4 2
7 0 0 -7
OutputCopy
7


strategy:
sort
greedy pick up


progress:
new problem solved it in 45 minutes

complexity

map - O(n)
filter - O(n)
sorted (n log n) i.e. do about log n comparations per n items
while - O(k)

worst case O(n log n) average O(k)

"""

_, k = list(map(int, input().split()))
arr = sorted(filter(lambda x: x < 0, (map(int, input().split()))))
res = 0
i = 0
while k >= 1 and i != len(arr):
    res += abs(arr[i])
    i += 1
    k -= 1
print(res)
