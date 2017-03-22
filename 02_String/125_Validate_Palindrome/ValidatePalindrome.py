class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Special cases
        if len(s) < 2: return True
        # Normal cases: two pointers (only consider letters)
        start_ptr, end_ptr = 0, len(s) - 1
        def validateAlphanumeric(a_chr):
            # If a number return true
            if a_chr >= 'a' and a_chr <= 'z' or a_chr >= 'A' and a_chr <= 'Z':
                return True
            # if a letter return true
            if a_chr >= '0' and a_chr <= '9':
                return True
            # if not both return false
            return False
        def convertToLowerCase(a_chr):
            if a_chr >= 'A' and a_chr <= 'Z':
                return chr(ord(a_chr) - ord('A') + ord('a'))
            return a_chr
        while start_ptr < end_ptr:
            start_chr, end_chr = s[start_ptr], s[end_ptr]
            if not validateAlphanumeric(start_chr): start_ptr += 1
            elif not validateAlphanumeric(end_chr): end_ptr -= 1
            elif convertToLowerCase(start_chr) != convertToLowerCase(end_chr): return False
            else: start_ptr, end_ptr = start_ptr + 1, end_ptr - 1
        return True
sol = Solution()
print sol.isPalindrome('')
print sol.isPalindrome('a')
print sol.isPalindrome('aa')
print sol.isPalindrome('ab')
print sol.isPalindrome('aA')
print sol.isPalindrome('abA')
print sol.isPalindrome('aBAb')
print sol.isPalindrome('1abA')
print sol.isPalindrome('ab1BA')
print sol.isPalindrome('aB2a')
print sol.isPalindrome('A man, a plan, a canal: Panama')