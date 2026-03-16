from lc import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2,2,1]))
