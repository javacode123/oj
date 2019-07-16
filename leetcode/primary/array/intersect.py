# coding: utf-8
# 给定两个数组，编写一个函数来计算它们的交集。
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
# 我们可以不考虑输出结果的顺序。
# 如果给定的数组已经排好序呢？你将如何优化你的算法？  使用两个指针，根据两个指针判断，时间复杂度 o(m)
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？ 对 nums2 做 hash
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？ 分段处理

class Solution(object):
    def intersect_v1(self, nums1, nums2):
        """
        solution: 使用循环的方法, 时间复杂度 o(n*n)
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if nums2 is None or nums1 is None:
            return res

        for i in nums1:
            if i in nums2:
                res.append(i)
                nums2.remove(i)

        return res

    def intersect(self, nums1, nums2):
        """
        solution: 使用 hash 的方法, 第二次不用遍历直接哈希, 使用空间节省时间, 时间复杂度 o(n)
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if nums2 is None or nums1 is None:
            return res

        nums1_dict = dict()

        for i in nums1:
            if nums1_dict.get(i):
                nums1_dict[i] += 1
            else:
                nums1_dict[i] = 1

        for i in nums2:
            if nums1_dict.get(i):
                res.append(i)
                if nums1_dict[i] == 1:
                    nums1_dict.pop(i)
                else:
                    nums1_dict[i] -= 1

        return res


if __name__ == '__main__':
    print Solution().intersect([1,2,2,1], [2, 2])

