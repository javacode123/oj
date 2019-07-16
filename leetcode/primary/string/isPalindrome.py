# coding: utf=8
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 说明：本题中，我们将空字符串定义为有效的回文串。
import string


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or s.strip() == '':
            return True

        word_dict = {chr(_): 0 for _ in range(97, 123)}
        word_dict.update(**{chr(_): 0 for _ in range(48, 58)})

        start, end = 0, len(s)-1

        while start < end:
            while word_dict.get(s[start].lower(), None) is None and start < end:
                start += 1

            while word_dict.get(s[end].lower(), None) is None and start < end:
                end -= 1

            if start < end:
                if s[start].lower() != s[end].lower():
                    return False
                else:
                    start += 1
                    end -= 1
        return True


if __name__ == '__main__':
    print Solution().isPalindrome("0P")
