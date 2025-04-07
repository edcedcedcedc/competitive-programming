"""

understanding:

Find (g, j) pairs that satisfy the following constraints:
The constraint: nums[g] - j  = nums[j] - g

g and j are indexes

[0 9 7 3 5]

strategy:

O(n^2)
for i in nums
    for j in nums
        invariant

O(n)
nums(g) - j = nums(j) - g
nums(g) + g = nums(j) + j

dict = {}

for i in nums:
    key = nums(i) + i
    dict[key].append(i)
"""

a = [0, 9, 3, 7, 5]

d = dict()

for i in range(len(a)):
    key = a[i] + i
    try:
        v = d[key]
        v.append(i)
    except:
        v = list()
        v.append(i)
        d[key] = v

r = []

for i in d.values():
    if len(i) > 1:
        arr = i
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j:
                    r.append(((arr[i]), arr[j]))
print(r)
