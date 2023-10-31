from typing import List


def max_profit(prices: List[int]) -> int:
    left, right = 0, 1
    profit = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            if prices[right] - prices[left] > profit:
                profit = prices[right] - prices[left]
        else:
            left = right
        right += 1
    return profit


if __name__ == '__main__':
    print(max_profit(prices=[7, 1, 5, 3, 6, 4]) == 5)
    print(max_profit(prices=[7, 6, 4, 3, 1]) == 0)
    print(max_profit(prices=[1, 4, 2]) == 3)
    print(max_profit(prices=[3, 2, 6, 5, 0, 3]) == 4)
    print(max_profit(prices=[1, 1, 1]) == 0)
