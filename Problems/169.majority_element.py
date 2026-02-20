from lc import *


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0,0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3,2,3]))
