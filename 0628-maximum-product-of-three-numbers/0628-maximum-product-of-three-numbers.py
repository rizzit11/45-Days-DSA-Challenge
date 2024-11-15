class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        product1 = nums[-1] * nums[-2] * nums[-3]
        product2 = nums[0] * nums[1] * nums[-1]
        
        return max(product1, product2)

# Approach: Pehle mujhe laga ki mujhe bas largest three numbers ko find karna hai to get the maximum product, but phir mujhe samajh aaya ki kuch negative numbers ho sakte hain jo product ko aur bhi bada bana sakein. For example, agar array mein do negative numbers hain, unka product positive ho jata hai, which can be larger when multiplied with a big positive number. Isliye maine array ko pehle sort kiya. After sorting, I had two options for maximum product: either take the largest three numbers, or take the two smallest (negative) numbers and multiply them with the largest positive number.

# Logic: Sorting the array allows us to easily identify the three largest values and the two smallest values. Maximum product is either the product of the three largest positive values (nums[-1] * nums[-2] * nums[-3]), or the product of the two smallest values (which could be negative) and the largest value (nums[0] * nums[1] * nums[-1]). The idea is to consider both cases and return the maximum of the two. This ensures that even if there are negative values, we are able to get the highest possible product.

