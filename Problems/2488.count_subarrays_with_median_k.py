from lc import *
from collections import defaultdict
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Find index where nums[i] == k
        pos = -1
        for i, v in enumerate(nums):
            if v == k:
                pos = i
                break

        # Step 1: build freq map of balances on the left side of k (including pos)
        balance = 0
        left_balance_count = defaultdict(int)
        left_balance_count[0] = 1  # empty prefix before we start

        for i in range(pos):
            if nums[i] < k:
                balance -= 1  # smaller than k
            elif nums[i] > k:
                balance += 1  # greater than k
            # store balance for prefix ending at i
            left_balance_count[balance] += 1

        # Step 2: now go from pos to end, updating balance and using map
        result = 0
        result += left_balance_count[balance]        # for total balance 0
        result += left_balance_count[balance - 1]    # for total balance 1

        for i in range(pos + 1, n):
            if nums[i] < k:
                balance -= 1
            elif nums[i] > k:
                balance += 1

            # Need total balance 0 or 1 for [some_left_index .. i]
            result += left_balance_count[balance]
            result += left_balance_count[balance - 1]

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.countSubarrays([3, 2, 1, 4, 5], 4))
