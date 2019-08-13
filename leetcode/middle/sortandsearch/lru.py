# -*- coding: utf-8 -*-
# @Time    : 2019-08-25 18:07
# @Author  : Zhangjialuo
# @mail    : zhang_jia_luo@foxmail.com
# @File    : lru.py
# @Software: PyCharm


class Cache():
    def __init__(self):
        self.cache = {}
        self.keys = []
        self.capacity = 4

    def put(self, key, value):
        if self.cache.get(key):  #更新
            self.cache[key] = value
        else:
            if len(self.keys) == self.capacity:  #淘汰
                remove_key = self.keys.pop(0)
                self.cache.pop(remove_key)
            self.cache[key] = value
            self.keys.append(key)
        return value

    def get(self, key):
        value = self.cache.get(key, None)
        if value:
            self.keys.remove(key)
            self.keys.append(key)  #最新访问 key 放在队列尾部
        return value


if __name__ == '__main__':
    cache = Cache()
    cache.put('1', '2')
    print(cache.get('1'))
    print(cache.get('1'))
    print(cache.get('1'))
    cache.put('2', '3')
    cache.put('3', '4')
    cache.put('4', '5')
    cache.put('5', '6')
    print('5', cache.get('5'))
    print('4', cache.get('4'))
    print('3', cache.get('3'))
    print('2', cache.get('2'))
    print('1', cache.get('1'))
    cache.put('8', '8')

    print('5', cache.get('5'))
    print('4', cache.get('4'))
    print('3', cache.get('3'))
    print('2', cache.get('2'))
    print('1', cache.get('1'))
    print('8', cache.get('8'))



