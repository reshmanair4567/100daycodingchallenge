def maxProfit(prices):
    if len(prices)==0:
        return 0
    max_profit=0
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            if prices[j]>prices[i]:
                profit=prices[j]-prices[i]
                if profit>max_profit:
                    max_profit=profit
    return max_profit
    
if __name__=="__main__":
    prices=[2,7,1,6,5,4]
    print(maxProfit(prices))


    '''
    if len(prices)==0:
            return 0
    mini=max(prices)
    maxprofit=0
    for i in range(len(prices)):
        if prices[i]<mini:
            mini=prices[i]
            
        elif prices[i]-mini >maxprofit:
            maxprofit=prices[i]-mini
            
    return maxprofit
'''





def maxProfit(prices):
        profit = 0
        for i in range(1, len(prices)) :
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i - 1]
        return profit