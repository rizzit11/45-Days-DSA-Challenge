class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

# Approach: Pehle mujhe laga ki mujhe har element ka count rakhna padega using a dictionary, but phir mujhe ek efficient algorithm yaad aaya—Boyer-Moore Voting Algorithm. Is algorithm mein hum ek candidate element ko track karte hain aur uska count maintain karte hain. Agar count zero ho jata hai, toh hum ek naya candidate pick karte hain. Yeh approach isliye kaam karta hai kyunki majority element hamesha n / 2 se zyada baar aayega, toh final candidate hamesha majority element hi hoga.

# Logic: We start with an initial candidate (candidate) and a count (count) set to zero. For each element in the array, agar count == 0 ho jaye, toh hum naya candidate pick karte hain as the current element. Agar current element candidate ke equal hai, toh count ko increase karte hain, otherwise count ko decrease kar dete hain. Is process ke baad jo final candidate bachega, wahi majority element hoga. Yeh algorithm O(n) time complexity mein kaam karta hai, aur space complexity O(1) hai, making it highly efficient.