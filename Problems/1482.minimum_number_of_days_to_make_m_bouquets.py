from lc import *
from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        
        if n < m * k:
            return -1  
        
        def can_make(day: int) -> bool:
            bouquets = 0
            consecutive = 0
            for d in bloomDay:
                if d <= day:
                    consecutive += 1
                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0
                else:
                    consecutive = 0
            return bouquets >= m  
        
        low, high = min(bloomDay), max(bloomDay)  
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_make(mid):
                ans = mid      
                high = mid - 1
            else:
                low = mid + 1  
        
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.minDays([1,10,3,10,2], 3, 1))