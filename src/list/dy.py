import sys

class Solution:
    #  斐波那契数
    ## 方法1
    def fib_1(self, n: int) -> int:
        if n == 0 or n == 1: return n
        dp_0 = 0
        dp_1 = 1

        for i in range(2, n+1):
            dp_i = dp_0 + dp_1
            dp_0 = dp_1
            dp_1 = dp_i

        return dp_1

    ## 方法2: dp table
    def fib_2(self, n: int) -> int:
        if n == 0 or n == 1: return n
        dp = [0, 1]
        for i in range(2, n+1):
            dp.append(dp[i-1] + dp[i-2])

        return dp[n]

    def fib_3(self, n: int) -> int:
        memo = []
        def dp(n , memo: list):
            if n == 0 or n == 1: return n
            if n in memo:
                return memo[n]
            memo.append(dp(n-1, memo) + dp(n-2, memo))
            return memo[n]

        return dp(n, memo)

    # 零钱兑换
    ## 方法1：暴力破解
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        if amount < 0: return -1

        res = sys.maxsize

        for coin in coins:
            sub_amount = self.coinChange(coins, amount - coin)
            if sub_amount == -1: continue
            res = min(res, sub_amount + 1)

        return res if res != sys.maxsize else -1


    ## 方法2： dp table
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount

        # 最小硬币为1，以为可以使用i遍历从0-amount 的硬币
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue

                dp[i] = min(dp[i], dp[i-coin] + 1)

        return -1 if dp[amount] == amount + 1 else dp[amount]


    ## 方法3： 备忘录
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-2] * (amount + 1)

        def dp(coins, amount):
            if amount ==0: return 0
            if amount < 0: return -1

            if memo[amount] != -2: return memo[amount]

            res = sys.maxsize
            for coin in coins:
                sub_amount = dp(coins, amount - coin)

                if sub_amount == -1:
                    continue
                res = min(res, sub_amount + 1)
            memo[amount] = res if res != sys.maxsize else -1
            return memo[amount]

        return dp(coins, amount)
