from lc import *


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.getConcatenation([1,2,1]))
