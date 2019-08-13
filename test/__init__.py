# -*- coding: utf-8 -*-
# @Time    : 2019-08-24 15:41
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : __init__.py.py
# @Software: PyCharm

import sys


if __name__ == '__main__':
    for line in sys.stdin:  # 读作数组
        m, n = [int(_) for _ in line.split()]  # 记录，班级数
        teach_dict = {}
        student_dict = {}
        recoder = {}
        teach_time = {}
        res = {}

        for i in range(n):
            line = input().split()
            teach_dict[line[2]] = line[1]
            student_dict[line[2]] = [_ for _ in line[3:]]
            res[line[2]] = 0

        for i in range(m):
            line = input().split()

            if recoder.get(line[1]):
                recoder[line[1]].append(int(line[2]))
            else:
                recoder[line[1]] = [int(line[2])]

        for class_n, t_id in teach_dict.items():
            teach_time[class_n] = [(recoder[t_id][i], recoder[t_id][i+1]) for i in range(len(recoder[t_id])//2)]
            tsum = sum(list(map(lambda x: x[1]-x[0], teach_time[class_n])))
            for s_id in student_dict[class_n]:
                for t in range(len(recoder.get(s_id, []))//2):
                    t1, t2 = recoder[s_id][t], recoder[s_id][t+1]
                    for t_tuple in teach_time[class_n]:
                        min_t = max(t_tuple[0], t1)
                        max_t = min(t_tuple[1], t2)
                        if max_t > min_t:
                            res[class_n] += (max_t-min_t)
            res[class_n] /= tsum*len(student_dict[class_n])

        a = sorted(res.items(), key=lambda x: x[1], reverse=True)

        print(a)

"""
12 2
3 999 yy1 0001 0002 0004
2 9988 yu\y2 0003 0009
IN 0001 9001
OUT 0001 9006
IN 999 8888
OUT 999 8888
IN 999 9003
OUT 999 9004
IN 9988 9005
OUT 9988 9008
IN 0003 9001
OUT 0003 9002
IN 0003 9005
OUT 0003 9006
"""

