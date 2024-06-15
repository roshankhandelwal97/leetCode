#https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m*k:
            return -1
        
        if len(bloomDay) == m*k:
            return max(bloomDay)

        left = min(bloomDay)
        right = max(bloomDay)
        
        answer = max(bloomDay)
        while(left <= right):
            mid = (left +right) // 2
            count = 0
            no_bouq = 0
            for j in range(len(bloomDay)):
                if bloomDay[j] - mid <= 0:
                    count += 1
                else:
                    no_bouq += count // k
                    count = 0
                if j == len(bloomDay)-1:
                    no_bouq += count // k
            if no_bouq >= m:
                answer = min(answer, mid)
                right = mid - 1
            else:
                left = mid + 1
        return answer
