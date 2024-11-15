class Solution:

    def findMinDiff(self, arr,M):
        
        arr.sort()
        min_difference = float('inf')
        
        for i in range(len(arr) - M + 1):
            current_difference = arr[i + M - 1] - arr[i]
            
            if current_difference < min_difference:
                min_difference = current_difference
        
        return min_difference

# Approach: Pehle mujhe laga ki mujhe sare combinations check karne padenge to find the smallest difference, but phir maine
        #   realize kiya ki yeh kaafi inefficient hoga. Instead, I decided to sort the array first. Sorting karne se mujhe 
        #   pata chala ki chocolates ke packets ko ek tarah se arrange kar ke hum consecutive subsets ko compare kar sakte 
        #   hain to find the minimum difference. Sorting ke baad, maine ek sliding window approach use kiya jahan maine "M"
        #   size ke consecutive packets liye aur har baar maximum aur minimum ke beech ka difference nikal ke dekha.
# Pehle kuch galtiyaan hui, jaise main manually multiple pointers use karne ka soch raha tha,but the i used Sliding window.

# Logic: Final approach yeh tha ki pehle hum array ko sort karenge taaki packets ek arranged order mein ho. Fir hum ek 
#        sliding window of size m use karenge. Har window ke andar hum pehla aur last element consider karenge aur unke
#        beech ka difference calculate karenge. Har step pe, hum minimum difference track karte hain. Yeh approach ensure
#      karta hai ki hum smallest possible difference find kar paye, efficiently aur bina kisi extra data structure ke. 
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        A = [int(x) for x in input().split()]
        M = int(input())

        solObj = Solution()

        print(solObj.findMinDiff(A, M))
        print("~")

# } Driver Code Ends