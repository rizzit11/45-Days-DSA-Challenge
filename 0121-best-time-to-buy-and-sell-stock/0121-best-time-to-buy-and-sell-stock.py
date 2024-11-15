class Solution:                                      
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit

#Approach: Initially, I thought of finding the minimum price by using min(prices), and then finding a corresponding maximum price. But I soon realized that this wouldn’t work because it would require multiple passes over the array, making the solution inefficient. After reconsidering, I realized that the goal was to dynamically track both the lowest price and the maximum profit as I looped through the array. This led me to adopt a single-pass solution that could handled everything in a go. At first, I made some mistakes trying to compare min_price directly without a dynamic approach. I also tried keeping a separate list to track minimums and profits, which ended up making things more complex and unnecessary. After refining my approach, I found a much cleaner solution.

#Logic: The final approach involves using one pointer (min_price) to track the lowest price seen so far, and one variable (max_profit) to store the best profit we can achieve. As I loop through the array of prices, I keep updating min_price whenever I find a new lower price. For each price, I calculate the potential profit (current price - min_price). If this profit is greater than the current max_profit, I update max_profit accordingly. This ensures that, by the end of the loop, I’ve found the maximum profit possible in just one pass through the array. It felt really satisfying to see how such an approach efficiently captured the core requirement of maximizing profit while keeping the solution elegant and simple.