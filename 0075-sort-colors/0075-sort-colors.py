class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Step 1: Initialize three helpers to sort (low, current, high)
        low, current, high = 0, 0, len(nums) - 1

        # Step 2: Loop until current crosses high
        while current <= high:
            if nums[current] == 2:
                # Found a blue ball (2), swap it with high and move high left
                nums[current], nums[high] = nums[high], nums[current]
                high -= 1  # Shrink the high zone
            elif nums[current] == 0:
                # Found a red ball (0), swap with low and move both low and current right
                nums[current], nums[low] = nums[low], nums[current]
                low += 1  # Expand the low zone
                current += 1  # Move to check the next ball
            else:
                # Found a white ball (1), just move current to the next one
                current += 1  # White stays in the middle zone

#------------x------------x------------x-----------x-----------x-----------x-----------x----------#

# LOGIC

#For this problem, we think of sorting the numbers as if we have three different buckets of colored balls.
#We have three helpers (“low”, “current”, and “high”) managing the placement of red (0), white (1), and blue (2) balls.

#low is responsible for keeping all the red balls at the beginning. Whenever we find a red ball (0), we swap it with the element at the low pointer, and then move both low and current pointers to the right.

#high is responsible for putting all blue balls at the end. Whenever we find a blue ball (2), we swap it with the element at the high pointer, then move the high pointer to the left. Importantly, we do not move current after swapping a blue ball, because we need to verify what the new element at current is.

#current checks every ball and decides what to do. When current finds a white ball (1), it just moves to the right, since white is already in the correct middle position.

#Using this step-by-step approach with three helpers, we can efficiently arrange all the balls into their correct colored zones in just one pass through the array.

