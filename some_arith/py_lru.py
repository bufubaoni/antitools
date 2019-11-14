# -*- coding: utf-8 -*-
# 一个简单的lru 缓存 python 中有本地存储python-lru库，请使用标准库


class SimpleLru(dict):

    def __init__(self, records_limit=100):
        self.records_limit = records_limit

    def get(self, key):
        if key in self.keys():
            hot_numbers = self[key].get('hot_numbers')
            hot_numbers += 1
            value = self[key].get('value')
            self[key] = {'hot_numbers': hot_numbers, 'value': value}
            return value
        else:
            raise AttributeError('not in this cache')

    def set(self, key, value):
        l_sort_keys = sorted([(k, v.get('hot_numbers'))for k, v in self.items()], lambda x, y: x[1] > y[1])
        if len(l_sort_keys) >= self.records_limit:
            _key, _ = l_sort_keys.pop(-1)
            self.pop(_key)
            self[key] = {'hot_numbers': 1, 'value': value}
        else:
            self[key] = {'hot_numbers': 1, 'value': value}


if __name__ == "__main__":
    local_cache = SimpleLru(2)

    local_cache.set('test', 1)
    local_cache.set('test2', 1)
    local_cache.set('test3', 3)
    local_cache.get('test')
    local_cache.get('test')
    local_cache['test3']
    local_cache.set('test4', 4)
    print local_cache
    print local_cache.get('test')
