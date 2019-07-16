# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-


def reverse_sentence(s):
        res = ''
        if s is None or s == [] or s == ' ':
            return s
        arr_s = s.split(' ')
        for word in arr_s[:: -1]:
            if word:
                word += ' '
                res += word
        return res[0:-1]


if __name__ == '__main__':
    s = " "
    print s == " "
    print s.split(' ')
    print reverse_sentence(s) == ' '
