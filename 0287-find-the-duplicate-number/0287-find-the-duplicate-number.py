class Solution:
    def findDuplicate(self, nums):
        # Step 1: Initialize turtle and rabbit at the starting line
        slow, fast = nums[0], nums[0]

        # Step 2: Rabbit moves twice as fast as the turtle until they meet inside the loop
        while True:
            slow = nums[slow]           # Turtle moves one step
            fast = nums[nums[fast]]     # Rabbit moves two steps
            if slow == fast:            # Rabbit catches the turtle
                break

        # Step 3: Reset turtle to start, both move at the same speed to find the entrance of the cycle
        slow = nums[0]
        while slow != fast:             # Turtle and rabbit race to find the duplicate
            slow = nums[slow]           # Turtle moves one step
            fast = nums[fast]           # Rabbit also moves one step
          
        return slow                     # The meeting point is the duplicate number

# LOGIC

#In this problem, we use the turtle and rabbit race analogy to find the duplicate number.

#We start with both the turtle (slow pointer) and the rabbit (fast pointer) at the starting line. They both begin at the first number of the array. The rabbit moves twice as fast as the turtle, helping us to quickly find a cycle in the sequence of numbers.

#Once the rabbit catches up with the turtle inside the cycle, we know there is a repeated number. Now, we need to find exactly where the cycle starts. So, we move the turtle back to the beginning and have both the turtle and rabbit move at the same speed until they meet again. The place they meet is the duplicate number.