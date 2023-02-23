#!/usr/bin/python3
from baseclass import BaseCaching

class BasicCache(BaseCaching):
    """A blueprint for basic caching algorithms"""

    def put(self, key, item):
        """ Adds an item to the caching dictionary"""
        if key == None or item == None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Gets an item from the caching dictionary"""
        if key == None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]



#TESTING TIME
if __name__ == '__main__':
    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D"))
    my_cache.print_cache()
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
