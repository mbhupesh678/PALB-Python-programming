class Solution:
    def minSwaps(self, s1, s2):
        count01=0
        count10=0
        for i in range(len(s1)):
            if s1[i]=='0' and s2[i]=='1':
                count01+=1
            elif s1[i]=='1' and s2[i]=='0':
                count10+=1
        ans=count01//2+count10//2 #two mismatches can be fixed with one swap
        #but odd mismatches need two swaps
        if count01%2==0 and count10%2==0:
            return ans #if both are even
        elif (count01+count10)%2==0:
            return ans+2 #if their sum is even but they are odd individually
        else:
            return -1 #impossible if total sum is odd
        return ans
