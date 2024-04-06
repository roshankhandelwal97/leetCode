#https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr= []
        for i,j in zip(position, speed):
            arr.append([i,j])
        arr = sorted(arr)
        stack = []

        def time(a):
            dist, speed = a
            time = ((target-dist)/speed)
            return time


        for i, j in arr[::-1]: 
            stack.append([i,j])
            if(len(stack) == 1):
                continue
            if(time(stack[-1]) <= time(stack[-2])):
                stack.pop()
        return len(stack)

