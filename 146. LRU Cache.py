#https://leetcode.com/problems/lru-cache/description/

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.queue = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        #rem = self.queue.pop(-1)
        if key in self.queue: 
            self.queue.remove(key)
            self.queue.append(key)
            return self.dic.get(key, -1)
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if(key in self.dic): 
            self.dic[key] = value
            self.queue.remove(key)
            self.queue.append(key)
        else: 
            if(len(self.queue) == self.capacity):
                rem = self.queue.pop(0)
                del self.dic[rem]
                self.queue.append(key)
                self.dic[key] = value
            else: 
                self.queue.append(key)
                self.dic[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
