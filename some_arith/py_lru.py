# -*- coding: utf-8 -*-
class SimpleLru(dict):

    def __init__(self, records_limit=100):
        self.records_limit = records_limit

    def get(self, key):
        if key in self.keys():
            hot_numbers = self.get(key).get('hot_numbers')
            hot_numbers += 1
            value = self.get(key).get('value')
            self.set(key, {'hot_numbers': hot_numbers, 'value': value})
            return value
        else:
            raise AttributeError('not in this cache')

    def set(self, key, value):
        l_sort_keys = [(k, v.get('hot_numbers'))for k, v in self.items()]
        if len(l_sort_keys) >= self.records_limit:
            _key, _ = l_sort_keys.pop(-1)
            self.pop(_key)
            self[key] = {'hot_numbers': 1, 'value': value}
        else:
            self[key] = {'hot_numbers': 1, 'value': value}


if __name__ == "__main__":
    local_cache = SimpleLru(2)

    local_cache.set('test', 2)
    local_cache.set('test2', 2)
    local_cache.set('test3', 2)
    local_cache['test']
    local_cache['test']
    local_cache['test3']
    local_cache.set('test4', 2)
