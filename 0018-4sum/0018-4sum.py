class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadruplets = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  

            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue 

                left, right = j + 1, len(nums) - 1

                while left < right:
                    total_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if total_sum == target:

                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif total_sum < target:

                        left += 1
                    else:

                        right -= 1

        return quadruplets

# Approach: Maine initially socha ki mujhe sab possible quadruplets check karne hain using four nested loops, but iska time complexity O(n⁴) ho jata, jo kaafi inefficient hota. Instead, maine ek better approach sochi using a combination of sorting and the two-pointer technique. Pehle array ko sort kiya, fir ek outer loop se har element fix kiya aur ek inner loop se doosra element fix kiya, uske baad two-pointer technique use ki to find the remaining two elements such that their sum matches the required value (target - (nums[a] + nums[b])). Sorting se mujhe duplicates handle karne mein bhi madad milti hai, taaki mujhe unique quadruplets milein.

# Logic: The sorted array allows us to easily navigate through the elements and avoid duplicates. Pehle do elements ko fix karne ke baad, hum remaining array pe two-pointer approach lagate hain. left pointer ko ek position pe set karte hain (b + 1) aur right pointer ko end par set karte hain. Hum unke sum ko check karte hain with the target value. Agar sum match ho jata hai, toh hum quadruplet ko result mein add karte hain aur left aur right pointers ko adjust karte hain duplicates ko avoid karne ke liye. Agar sum kam hota hai, toh left ko increase karte hain; agar sum zyada hota hai, toh right ko decrease karte hain. This approach helps to efficiently find all unique quadruplets with a time complexity of approximately O(n³).

