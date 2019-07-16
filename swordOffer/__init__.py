# coding=utf-8
target = 9
nums = [2, 7, 9]
d = dict()

for i in range(len(nums)):
    n = target - nums[i]
    if d.get(n, None) is not None:
        print [d.get(n), i]
    d[nums[i]] = i

print []