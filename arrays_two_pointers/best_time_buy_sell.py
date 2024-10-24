'''
You are given an array prices where prices[i] is the 
price of a given stock on the ith day.

You want to maximize your profit by choosing a single 
day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.
'''

# sliding window type deal
# Greedy algorithm, makes locally optimal choices at each step to find
# the globally optimal solution. "take best option now"

def max_profit(prices):
    l, r = 0, 1

    max_p = 0

    while r != len(prices):

        if prices[l] < prices[r]:

            profit = prices[r] - prices[l]
            max_p = max(max_p, profit)

        else:

            l = r
            
        r += 1

    return max_p

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(max_profit(prices))