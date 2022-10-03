class Solution:
    def NGR(self,nums2):
        s = []
        result = []
        for i in range(len(nums2)-1,-1,-1):
            if(len(s)==0 and i==len(nums2)-1):
                result.append(-1)
                s.append(nums2[i])
            elif(len(s)!=0 and s[len(s)-1]>nums2[i]):
                result.append(s[len(s)-1])
            elif(len(s)!=0 and s[len(s)-1]<=nums2[i]):
                while(len(s)!=0 and s[len(s)-1]<=nums2[i]):
                    s.pop()
                if(len(s)==0):
                    result.append(-1)
                else:
                    result.append(s[len(s)-1])
            s.append(nums2[i])
        result.reverse()
        return result 
    
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        dictionary = {}
        ngr_result = self.NGR(nums2)
        for nums, values in zip(nums2,ngr_result):
            dictionary[nums] = values
        for nums in nums1:
            ans = dictionary[nums]
            result.append(ans)
        return result