# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.

prices = [1,2,3,4,5]

max_prof = 0

min_prices = prices[0]

for i in range(1,len(prices)):
    if prices[i] < min_prices:
        min_prices=prices[i]
    max_prof=max(max_prof,prices[i]-min_prices)
    
print(max_prof)
