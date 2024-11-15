class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        j = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[j-1]:
                nums[j] = nums[i]
                j += 1
        return j

#Approach: Initially, I thought of using a set to remove the duplicates since sets automatically ensure that all elements are unique. However, I quickly realized that this approach wouldn’t work because the question specifically asked for an in-place solution—meaning no extra data structures—and the relative order needed to be maintained. Sets, as we know, don’t guarantee order, and creating one would mean extra space. After this realization, I pivoted to a different plan. I decided to use a two-pointer approach to handle this in-place. At first, I made some errors by trying to pop elements or swap incorrectly, but I eventually figured out a cleaner way using two pointers effectively.

#Logic: The final approach I used involved two pointers—one to scan through the entire array (i), and the other (j) to track the position for unique elements. Pointer j starts from index 1, assuming the first element is always unique. Pointer i starts scanning from the second element. Every time i finds a number that is different from the previous unique value (tracked by j - 1), I place that value at position j and move j to the next position. This way, all unique values get moved to the beginning of the array in a single pass, without requiring any additional data structures. The value of j at the end gives the count of unique elements.
 