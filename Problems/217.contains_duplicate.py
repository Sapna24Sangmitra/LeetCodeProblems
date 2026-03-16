from lc import *


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)

        return False

if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1,2,3,1]))
