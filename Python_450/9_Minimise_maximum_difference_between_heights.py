class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        mi=0
        ma=0
        result=arr[n-1] - arr[0]
        for i in range(1,n):
                ma=max(arr[i-1] + k, arr[n-1]-k)
                mi=min(arr[0]+k, arr[i]-k)
                result=min(result,ma-mi)
        return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = 2
        n = 6
        arr = [2,4,6,1,9,3]
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        tc -= 1
    print(ans)
# } Driver Code Ends