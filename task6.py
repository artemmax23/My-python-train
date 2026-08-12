import time

class Cache:
    def __init__(self):
        self.__storage = dict()
        
    def set(self, key: str, value: object, ttl=10):
        if (ttl <= 0):
            return
        self.__storage[key] = {'value': value, 'expired_time': (time.time() +  ttl)}
        
    def has(self, key: str) -> bool:
        if key not in self.__storage: 
            return False
        if time.time()  > self.__storage[key]['expired_time']:
            del self.__storage[key]
            return False
            
        return True
        
        
    def get(self, key: str) -> object:
        if self.has(key):
            return self.__storage[key]['value']
            
        return None
        
cache = Cache()

cache.set('a', 1, 5)  # Живет 5 секунд
print(cache.get('a'))     # 1

time.sleep(3)             # Подождали 3 секунды
print(cache.get('a'))     # 1 (еще не истекло)

time.sleep(3)             # Подождали еще 3 секунды (всего 6)
print(cache.get('a'))     # None (истекло)