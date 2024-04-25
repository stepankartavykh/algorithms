def coin_change(coins, amount):
    def backtrack(remaining):
        if remaining < 0:
            return -1
        if remaining == 0:
            return 0
        if remaining in memo:
            return memo[remaining]

        min_coins = float('inf')

        for coin in coins:
            result = backtrack(remaining - coin)
            if result >= 0:
                min_coins = min(min_coins, result + 1)

        memo[remaining] = min_coins if min_coins != float('inf') else -1
        return memo[remaining]

    memo = {}
    return backtrack(amount)


if __name__ == '__main__':
    print(coin_change([186, 419, 83, 408], 6249))
    print(coin_change([1, 2, 5], 11))
    print(coin_change([2], 3))
    print(coin_change([1], 0))
