class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j=0 # Non - zero pointers ko track karne ke liye

        for i in range(len(nums)): # yeh wala i ke through array mai iterate karega
            if nums[i] != 0: # to check if the number is not equal to zero
                nums[j] = nums[i] #j ke posi pe non-zero elements ko swap karne ke liye
                j += 1 # after the swap, i automatically increment hoga since for loop mai "i" iterate
                       #ho raha so we need to increment j to next position for the next non-zero element

        for k in range(j, len(nums)): #to fill remaining positions with zeros asked asked in question
            nums[k] = 0    

# Approach: At first, I thought about simply popping out all the zeros and appending them to the end of the array. But then I realized this approach wasn’t efficient at all, and it went against the requirement of modifying the array in-place without using additional data structures. Plus, manually shifting elements was prone to error and could easily mess up the relative order of non-zero elements. After some trial and error, I shifted towards a two-pointer approach. Initially, I tried swapping zeros and non-zero elements directly whenever I found them, but it didn’t give me the smooth results I needed. It made more sense to have a dedicated pointer (j) that would track the position where each non-zero value should go. 

# Logic: The final solution involved two pointers. Pointer i scans through every element of the array from start to finish, and Pointer j keeps track of where the next non-zero element should be placed. Every time i finds a non-zero element, I move it to position j and then increment j so it’s ready for the next non-zero value. After all non-zero values are moved to the start, the rest of the array from j to the end is filled with 0s.  