from lc import *


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9 + 7

        inventory.sort()
        n = len(inventory)
        res = 0
        orders_left = orders

        for i in range(n - 1, -1, -1):
            cur = inventory[i]
            prev = inventory[i - 1] if i > 0 else 0
            diff = cur - prev  

            bars = n - i               
            max_take = diff * bars     

            take = min(orders_left, max_take)

            full_layers = take // bars
            remainder = take % bars

            high = cur
            low = cur - full_layers

            total_full = (high * (high + 1) // 2) - (low * (low + 1) // 2)
            res += (total_full * bars) % MOD

            res += (remainder * low) % MOD
            res %= MOD

            orders_left -= take
            if orders_left == 0:
                break

        return res % MOD


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([2,5],4))
