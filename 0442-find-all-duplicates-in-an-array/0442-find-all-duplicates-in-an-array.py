class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            index = abs(num) - 1
            
            if nums[index] < 0:
                result.append(abs(num))
            else:
                nums[index] = -nums[index]
                
        return result


# Approach: Maine initially socha ki ek two-pointer approach use karun jahan ek pointer i start ho 0 se aur j start ho 1 se, but mujhe realise hua ki yeh time complexity ko O(n²) tak le ja sakta hai. Instead, I used the property of the values to mark indices. We iterate over the array, and for each number, we treat its value as an index and mark that index as visited by flipping it to negative. If we see a value pointing to an already negative index, then we know it’s a duplicate.

# Logic: The idea is to use the values in the array as markers to track duplicates. We iterate through each element of the array, and for each number (num), we compute its corresponding index (abs(num) - 1). If the value at that index is negative, it indicates that we have seen this number before, so it is a duplicate, and we add it to our result list. Otherwise, we mark that index by making the value negative, ensuring that the first time we visit an index, we keep track of it. This approach ensures we use O(1) extra space and O(n) time, meeting the problem requirements efficiently.