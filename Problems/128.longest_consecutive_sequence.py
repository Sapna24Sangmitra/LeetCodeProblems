from lc import *


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in numSet:
            # check if its start of the sequence
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([100,4,200,1,3,2]))
