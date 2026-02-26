class Solution:
    def missingRange(self, arr, low, high):
        #code hereclass Solution:
      s=set(arr)
      ans=[]
      for i in range(low,high+1):
        if i not in s:
          ans.append(i)
      return ans
