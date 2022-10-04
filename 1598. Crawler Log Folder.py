class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        operations = set(["../","./"])
        for char in logs:
            if char not in operations:
                stack.append(char)
            elif(len(stack)!=0):
                if(char=="../"):
                    stack.pop()
                elif(char=="./"):
                    continue
                else:
                    return -1
        return len(stack)