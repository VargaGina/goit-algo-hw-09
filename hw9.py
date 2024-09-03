def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    coin_count= {}
    
    for coin in coins:
        if amount >=coin:
            coin_count[coin]=amount//coin
            amount %= coin 
    
    return coin_count

def find_min_coins(amount):
    coins = [50,25,10,5,2,1]
    min_coins=[float('inf')]*(amount+1)
    min_coins[0]=0

    last_coin=[0]*(amount+1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i-coin]+1<min_coins[i]:
                min_coins[i]=min_coins[i - coin] + 1
                last_coin[i] = coin

    coin_count= {}
    while amount > 0:
        coin = last_coin[amount]
        if coin in coin_count:
            coin_count[coin] += 1
        else:
            coin_count[coin] = 1
        amount -= coin

    return coin_count

find_coins_greedy(111)

find_min_coins(111)


