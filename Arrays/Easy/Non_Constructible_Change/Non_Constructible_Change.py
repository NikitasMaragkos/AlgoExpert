def nonConstructibleChange(coins):
    coins.sort()
    currentChange = 0
    for aCoin in coins:
        if aCoin > currentChange + 1:
            return currentChange + 1
        currentChange += aCoin
return currentChange + 1