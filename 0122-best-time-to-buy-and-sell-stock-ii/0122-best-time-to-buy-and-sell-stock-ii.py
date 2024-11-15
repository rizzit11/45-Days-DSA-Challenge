class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]

        return total_profit

# Approach: Initially, I thought that I needed to find the lowest price to buy and then look for the best price to sell, similar to the first version of the problem. But then I realized, yahan pe mujhe multiple transactions karne ki permission hai, which means we can buy and sell multiple times to maximize profit. Iska matlab yeh hai ki jab bhi price increase ho raha hai, tab humein sell karke profit banana chahiye, chahe woh chota profit hi kyun na ho. So, the strategy is simple: traverse through the price array and whenever you see that the current day's price is greater than the previous day's price (prices[i] > prices[i-1]), calculate the profit (prices[i] - prices[i-1]) and add it to total_profit. Yeh approach ensure karta hai ki hum saare small profits ko add karein, jisse final profit maximize ho jaye. This way, by taking advantage of all the price increases, we end up with the maximum possible profit.

# Logic: The key to solving this problem is to treat every upward movement in the stock prices as an opportunity to make a profit. Hum prices array ko ek ek din traverse karenge. Jab bhi humein lage ki prices[i] > prices[i-1], iska matlab hai ki price mein increase hua hai, aur yahan profit kamaya jaa sakta hai. Isliye hum us din ka profit calculate karenge (prices[i] - prices[i-1]) and add it to the total_profit. This greedy approach helps us accumulate profit from every small increase, ensuring that we maximize our overall profit at the end. So, instead of waiting for a big peak to sell, hum har small rise pe sell kar dete hain, which ultimately gives us the highest total profit.

