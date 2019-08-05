# coding: utf-8
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？


class Solution(object):
    def singleNumber(self, nums):
        """
        solution: 从题意可以看出，每个元素均出现两次，只有一个出现一次，可以使用位运算，相同为 0， 不同为 1
            & 运算：同为 1 为 1， 其余为 0
            | 运算：有一个 1 为 1， 其余为 0
            ^ 运算： 不同为 1，相同为 0
            在此题目中，根据异或运算的结合率，将相同位置为 0，不同位置为 0，即重复的置为 0，留下那个唯一的
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return None

        res = nums[0]

        for i in range(1, len(nums)):
            res = res ^ nums[i]

        return res


if __name__ == '__main__':
    print(Solution().singleNumber([1, 1, 3]))