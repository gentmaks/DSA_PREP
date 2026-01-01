class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            curr = digits[i]
            if curr + carry == 10:
                res.append(0)
            else:
                res.append(curr + carry)
                carry = 0
        if carry:
            res.append(1)
        return res[::-1] 
        