#https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = []
        res = []
        pro1 = 1
        pro2 = 1

        i = 0
        j = len(nums) - 1

        while(i < len(nums)):
            pro1 = pro1*nums[i]
            pro2 = pro2*nums[j]
            pre.append(pro1)
            post.append(pro2)
            i += 1
            j -= 1

        i = 0
        post = post[::-1]
        # print(pre, post)

        while(i < len(nums)):
            if(i == 0):
                res.append(post[1])
            elif (i == len(nums) -1):
                res.append(pre[i-1])
            else: 
                # print(i)
                # print(pre[i-1], post[i+1])
                res.append(pre[i-1]*post[i+1])
            i +=1
        return res





        
