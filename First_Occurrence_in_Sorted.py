class Solution:
    def firstSearch(self, arr, k):
        low, high = 0, len(arr) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == k:
                ans = mid
                high = mid - 1   # keep searching left side
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
