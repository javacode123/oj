# coding:utf-8
class Solution(object):
    def removeDuplicates(self, nums):
        """
        solution:
            声明变量 index = 0 表示未重复数组的下标，遍历数组，如果发现数组值与 nums[index] 不同，则赋值 nums[index+1]
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        index = 0  # 不重复数组下标

        for i in range(len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]

        return index+1


if __name__ == '__main__':
    print(Solution().removeDuplicates([1, 2, 2, 3]))