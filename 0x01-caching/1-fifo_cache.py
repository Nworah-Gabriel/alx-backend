##!/usr/bin/python3
"""A FIFO caching algorithm module"""
from baseclass import BaseCaching

class FIFOCache(BaseCaching):
    """ A baic caching algorithm that implements the FIFO principle"""
    
    storage_list = []

    def count(self):
        """Counts key pairs present in the caching dictionary"""
        value = 0
        for i in self.cache_data.keys():
            value += 1
        return value


    def put(self, key, item):
        """ Adds an item to the caching dictionary"""
        if key == None or item == None:
            return
        number = self.count()
        
        if number >= BaseCaching.MAX_ITEMS:
            first_data = self.storage_list.pop(0)
            del self.cache_data[first_data]
            print('DISCARD: {}'.format(first_data))
        
        self.cache_data[key] = item
        self.storage_list.append(key)
    

    
    def get(self, key):
        """ Gets an item from the caching dictionary"""
        if key == None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]


#TESTING TIME
if __name__ == '__main__':
    my_cache = FIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
