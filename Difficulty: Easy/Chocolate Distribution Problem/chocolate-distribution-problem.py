class Solution:

    def findMinDiff(self, arr,M):
        
        arr.sort()
        min_difference = float('inf')
        
        for i in range(len(arr) - M + 1):
            current_difference = arr[i + M - 1] - arr[i]
            
            if current_difference < min_difference:
                min_difference = current_difference
        
        return min_difference
        
        
        
        
        
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