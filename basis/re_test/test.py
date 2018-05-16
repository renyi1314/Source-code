class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        for i in range(len(A)):
            A = A[1:] + A[0]
            if A == B:
                return True
        return False


A = "abcde"
B = "abcde"
a = Solution()
c = a.rotateString(A, B)

print(c)
