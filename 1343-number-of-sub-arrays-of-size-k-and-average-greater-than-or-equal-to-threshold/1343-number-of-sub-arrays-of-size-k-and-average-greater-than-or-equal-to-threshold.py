class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        count=0
        s=sum(arr[:k])
        if s >=k* threshold:
            count+=1
        for i in  range (k,len(arr)):
            s+=arr[i]
            s-=arr[i-k]
            if s>= k * threshold:
                count+=1
        return count 


        extra=sum
        
        