# ============================================
# FREQUENCY COUNT USING HASHMAP (dict) IN PYTHON
# ============================================

# Take runtime user input
nums = list(map(int, input("Enter numbers: ").split()))


# --------------------------------------------
# WAY 1: Basic dictionary + if-else
# --------------------------------------------
freq1 = {}
for n in nums:
    if n in freq1:
        freq1[n] += 1
    else:
        freq1[n] = 1

print("\nWay 1 (if-else):")
print(freq1)


# --------------------------------------------
# WAY 2: Using dict.get() (cleaner)
# --------------------------------------------
freq2 = {}
for n in nums:
    freq2[n] = freq2.get(n, 0) + 1

print("\nWay 2 (dict.get()):")
print(freq2)


# --------------------------------------------
# WAY 3: Using collections.Counter (BEST)
# --------------------------------------------
from collections import Counter

freq3 = Counter(nums)

print("\nWay 3 (Counter):")
print(freq3)


# --------------------------------------------
# WAY 4: Using a defaultdict
# --------------------------------------------
from collections import defaultdict

freq4 = defaultdict(int)
for n in nums:
    freq4[n] += 1

print("\nWay 4 (defaultdict):")
print(dict(freq4))   # printing as normal dict


# --------------------------------------------
# WAY 5: Using dictionary comprehension
# (Not preferred but still possible)
# --------------------------------------------
freq5 = {n: nums.count(n) for n in set(nums)}

print("\nWay 5 (dict comprehension):")
print(freq5)


# --------------------------------------------
# WAY 6: Manual loop with set to avoid repeats
# (Old-school, not efficient)
# --------------------------------------------
freq6 = {}
unique = set(nums)

for u in unique:
    freq6[u] = 0
    for x in nums:
        if x == u:
            freq6[u] += 1

print("\nWay 6 (nested loops):")
print(freq6)
