# coding: utf-8
class Solution(object):
    def rotate(self, nums, k):
        """
        solution: 数组翻转，要求空间复杂度为 1
            1：ab --> ba 通过 （a的逆置矩阵b的逆置矩阵）的逆置求的
            2：循环移动
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if nums is None or len(nums) == 0 or k > len(nums):
            return

        '''
        for i in range(k):
            self.reverse_v2(nums)
        '''
        self.reverse(nums, 0, len(nums)-k-1)
        self.reverse(nums, len(nums)-k, len(nums)-1)
        self.reverse(nums, 0, len(nums)-1)

    def reverse(self, nums, left, right):
        """
        数组翻转
        :param nums:
        :param left:
        :param right:
        :return:
        """
        while left < right:
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
            right -= 1
            left += 1

    def reverse_v2(self, nums):  # 每个数的位置向后移动一次
        count = len(nums)
        temp = nums[0]

        for i in range(count-1, 0, -1):
            nums[(i+1) % count] = nums[i]

        nums[1] = temp


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    Solution().rotate(nums, 3)
    print(nums)
