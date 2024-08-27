"""
Best Time to Buy and Sell Stock (at most one transaction allowed)

Given an array prices[] of length N, representing the prices
of the stocks on different days, the task is to find the maximum profit
possible by buying and selling the stocks on different days
when at most one transaction is allowed.

Note: Stock must be bought before being sold.

Constraints:
-) 1 <= prices.length <= 10^5
-) 0 <= prices[i] <= 10^4
"""

tests = [
    ([1], 0),
    ([4, 2], 0),
    ([2, 4], 2),
    ([7, 1, 5, 3, 6, 4], 5),  # buy for 1, sell for 6
    ([7, 6, 4, 3, 1], 0),
    ([4, 3, 8, 1, 5], 5),  # buy for 3, sell for 8
]


def max_profit_first(lst: list[int]) -> int:
    """
    Idea:
    In order to maximize the profit,
    we have to minimize the cost price and maximize the selling price.

    So at every step, we will keep track of the minimum buy price of stock
    encountered so far.
    If the current price of stock is lower than the previous buy price,
    then we will update the buy price,
    else if the current price of stock is greater than the previous buy price
    then we can sell at this price to get some profit.
    After iterating over the entire array, return the maximum profit.
    """
    n = len(lst)
    assert n > 1
    i_buy = 0
    profit_max = 0
    for i in range(n):
        if lst[i] > lst[i_buy]:
            profit_max = max(profit_max, lst[i] - lst[i_buy])
        elif lst[i] < lst[i_buy]:
            i_buy = i
    return profit_max


def max_profit(prices: list[int]) -> int:
    price_min = prices[0]
    profit = 0
    for price in prices[1:]:
        price_min = min(price_min, price)
        profit = max(profit, price - price_min)
    return profit


if __name__ == "__main__":
    for lst, exp in tests:
        act = max_profit(lst)
        assert act == exp
