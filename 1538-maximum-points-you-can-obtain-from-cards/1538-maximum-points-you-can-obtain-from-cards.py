class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum = sum(cardPoints[:k])
        max_points = left_sum
        
        n = len(cardPoints)
        for i in range(1, k+1):

            left_sum = left_sum - cardPoints[k - i] + cardPoints[n-i]
            
            max_points = max(max_points, left_sum)
        
        return max_points