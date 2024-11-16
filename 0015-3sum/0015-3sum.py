class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]

                if total_sum == 0:

                    result.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result




# Approach: Pehle mujhe laga ki mujhe sab possible triplets check karne hain using nested loops, but mujhe samajh aaya ki iska time complexity O(n³) ho jayega, jo kaafi inefficient hai. Instead, maine ek efficient strategy use ki—sort the array first and then use the two-pointer technique. Sorting se mujhe easily pata chalega ki duplicate values ko kaise skip karna hai. Main ek loop mein ek pointer (i) set karta hoon, aur uske aage do pointers (left and right) use karta hoon to find the required triplets by summing them to zero. Har baar jab mujhe triplet milta hai, mai left aur right pointers ko aage move karke duplicates skip karta hoon to ensure unique triplets.

# Logic: The sorted array allows us to effectively use two pointers (left and right) to find the required triplets. For each i, we set left to i + 1 and right to the end of the array. If the sum of nums[i] + nums[left] + nums[right] is zero, we add the triplet to the result. Agar sum zero se kam hai, toh left ko increase karte hain taaki sum bade; agar sum zero se zyada hai, toh right ko decrease karte hain taaki sum kam ho. This approach efficiently finds all unique triplets that sum to zero with a time complexity of O(n²).

