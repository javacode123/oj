# coding: utf-8
# 给定一个整数数组，判断是否存在重复元素。
# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。


class Solution(object):
    def containsDuplicate(self, nums):
        """
        solution: 使用 hash 或者 set, hash 的效率更高一点，使用 set 的话，每次加入，查询都要使用二叉树
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False

        res_dict = dict()
        for i in nums:
            if res_dict.get(i):
                return True
            else:
                res_dict[i] = 1

        return False


if __name__ == '__main__':
    print(Solution().containsDuplicate([1,2,3,1]))
