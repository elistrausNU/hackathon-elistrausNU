def maxProfit(prices):
    max_price = 0
    for i in range(len(prices)):
        j = i+1
        local_max = 0
        while(j<len(prices)):
            if prices[j]>prices[i]:
                local_max = max(local_max, prices[j]-prices[i])
            j = j+1
        max_price = max(max_price, local_max)

    print("Return value: ", max_price)


if __name__ == "__main__":
    maxProfit([7,1,5,3,6,4])