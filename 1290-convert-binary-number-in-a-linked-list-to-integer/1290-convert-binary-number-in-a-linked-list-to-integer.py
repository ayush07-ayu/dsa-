class Solution:
    def getDecimalValue(self, head):
        result = 0
        ptr = head

        while ptr is not None:
            result = result * 2 + ptr.val
            ptr = ptr.next

        return result