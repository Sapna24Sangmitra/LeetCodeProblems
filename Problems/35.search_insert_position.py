from lc import *

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return l


if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1,3,5,6], 5))
