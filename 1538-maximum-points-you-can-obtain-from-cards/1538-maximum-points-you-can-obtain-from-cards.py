class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum = sum(cardPoints[:k])
        max_points = left_sum
        
        n = len(cardPoints)
        for i in range(1, k+1):

            left_sum = left_sum - cardPoints[k - i] + cardPoints[n-i]
            
            max_points = max(max_points, left_sum)
        
        return max_points

#Approach: Pehle mujhe laga ki main ya toh first k cards ya last k cards pick karke compare karoon. Lekin baad mein samajh aaya ki best solution ke liye humein kuch cards front se aur kuch end se bhi lene ka option explore karna chahiye. So, maine ek sliding window approach socha. Sabse pehle maine first k cards ka sum calculate kiya, usko mera initial sum maana. Fir ek-ek card left se remove karke, right se add karta gaya. Iss sliding window se hum efficiently check kar sakte hain ki max sum kaise mil sakta hai bina pura sum baar baar calculate kiye.

#Logic: Is problem ko solve karne ke liye maine sliding window ka use kiya. Pehle first k elements ka sum calculate kiya, jisse mujhe starting value mil gayi for max_points. Fir maine window ko slide kiya by removing one card from the left and adding one from the right, taaki saare possible combinations explore ho sakein. Har baar left_sum ko adjust karke check kiya ki kya yeh new sum max_points se zyada hai. Is approach ki time complexity O(k) hai kyunki hum sirf k elements ko traverse kar rahe hain.