class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        nsr = []
        result = []
        for i in range(len(prices)-1,-1,-1):
            if(len(stack)==0 and i==len(prices)-1):
                nsr.append(0)
                stack.append(prices[i])
            elif(len(stack)!=0 and stack[len(stack)-1]<=prices[i]):
                nsr.append(stack[len(stack)-1])
            elif(len(stack)!=0 and stack[len(stack)-1]>prices[i]):
                while(len(stack)!=0 and stack[len(stack)-1]>prices[i]):
                    stack.pop()
                if(len(stack)==0):
                    nsr.append(0)
                else:
                    nsr.append(stack[len(stack)-1])
            stack.append(prices[i])
        nsr.reverse()
        for i in range(len(prices)):
            ans = prices[i]-nsr[i]
            result.append(ans)
        return result
    