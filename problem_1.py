from collections import OrderedDict


class LRU_Cache:

    def __init__(self, capacity=5):
        self.capacity = capacity
        self.current_storage = 0
        self.cache = OrderedDict()

    def get(self, key):
        if type(key) != int:
            return -1
        if key in self.cache:
            self.set(key)  # This will update usage order
            return self.cache[key]
        return -1

    # Set method will receive just 1 arg, as key & value corresponds to
    # the same value, avoiding edge cases with different key & value:
    def set(self, value):
        if type(value) != int:
            return
        # If key in self.cache, delete key to re-add it and update usage
        if value in self.cache:
            self.cache.pop(value)
            self.current_storage -= 1

        if self.current_storage < self.capacity:
            self.cache[value] = value
            self.current_storage += 1
        else:  # current_storage will remain the same
            self.__remove()
            self.cache[value] = value

    def __remove(self):
        self.cache.popitem(last=False)


# TEST CASE 1:
print('TEST CASE 1:')
our_cache = LRU_Cache(5)

our_cache.set(1)
our_cache.set(2)
our_cache.set(3)
our_cache.set(4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5)
our_cache.set(6)

print(our_cache.get(3))  # returns -1

# TEST CASE 2:
print('TEST CASE 2:')
second_cache = LRU_Cache()

second_cache.set(10)
second_cache.set(20)
second_cache.set(30)
second_cache.set(None)  # Won't be added to the cache
second_cache.set('')  # Won't be added to the cache
second_cache.set(' ')  # Won't be added to the cache

print(second_cache.get(10))  # returns 10
print(second_cache.get(20))  # returns 20
print(second_cache.get(10))  # returns 10

second_cache.set(40)
second_cache.set(50)

print(second_cache.get(30))  # returns 30

second_cache.set(60)

print(second_cache.get(20))  # returns -1

# TEST CASE 3:
print('TEST CASE 3:')
third_cache = LRU_Cache(10)  # It can receive a size different than 5

third_cache.set(1)
third_cache.set(20)
third_cache.set(300)
third_cache.set(3.14159)  # Will not be added to the cache
third_cache.set(1010101010100000000001)
third_cache.set(89788845647899987454478547412144445)

print(third_cache.get(300))  # returns 300
print(third_cache.get(3.14159))  # returns -1
print(third_cache.get(1010101010100000000001))
# returns 1010101010100000000001

print(third_cache.get(89788845647899987454478547412144445))
# returns 89788845647899987454478547412144445

third_cache.set(60)
third_cache.set(700)
third_cache.set(8000)
third_cache.set(90000)
third_cache.set(100000)
third_cache.set(300)  # This already exists, so will just be updated

print(third_cache.get(100000))  # returns 100000
print(third_cache.get(300))  # returns 300
print(third_cache.get(1))  # returns 1

third_cache.set(20000000000)

print(third_cache.get(20000000000))  # returns 20000000000
print(third_cache.get(20))  # returns -1 as (20, 20) was removed
