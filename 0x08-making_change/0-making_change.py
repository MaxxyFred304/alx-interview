#!/usr/bin/python3


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.
    :param coins: list of integers representing the values of the coins in your possession
    :param total: integer representing the amount you want to make change for
    :return: fewest number of coins needed to meet total
             If total is 0 or less, return 0
             If total cannot be met by any number of coins you have, return -1
    """
    if total < 0:
        return 0
    if total == 0:
        return 0
    min_coins = float('inf')
    for coin in coins:
        if total - coin >= 0:
            num_coins = makeChange(coins, total - coin)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins + 1 if min_coins != float('inf') else -1
