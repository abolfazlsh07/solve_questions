def main():
    coin_m, gem_m = map(int, input().split())  # Input mario Coin and gem
    coin_s, gem_s = map(int, input().split())  # Input sword coin and gem
    rate = int(input())  # input rate
    can_buy_sword = False

    if coin(coin_m, coin_s, rate, gem_m) == True and  gem(gem_m, gem_s, rate, coin_m) == True:
        can_buy_sword = True

    if can_buy_sword:
        print("Yes")

    else:
        print("No")


def coin(coin_m, coin_s, rate, gem_m):
    s = coin_m
    if coin_s > coin_m:
        for i in range(1, gem_m + 1):
            n = i * rate
            gem_m -= 1

            if n + s > coin_s:
                coin_m += n
                return True

    elif coin_m >= coin_s:
        return True

    return False

def gem(gem_m, gem_s, rate, coin_m):
    if gem_s > gem_m:
        for i in range(1, coin_m + 1):
            coin_m -= rate * i
            gem_m += 1

            if gem_m >= gem_s:
                return True
    elif gem_s <= gem_m:
        return True

    return False

main()