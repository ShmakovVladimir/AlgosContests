def make_exchange(money, coins):
    coins.sort()
    if len(coins) == 0:
        return 0
    if money == coins[0]:
        return 1
    return make_exchange(money-coins[len(coins)-1],coins)+make_exchange(money,coins[:len(coins)-1])