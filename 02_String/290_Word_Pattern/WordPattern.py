class Solution(object):
    def wordPattern(self, pattern, _str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # Invalid cases
        if not _str or not pattern: return False
        words = _str.split(" ")
        # Special case
        if len(words) != len(pattern): return False
        n = len(words) # n is length of both words and str
        # Must find a way to map a character with a word (a char must be mapped one-to-one and onto with a word)
        # Therefore, must create two hashes
        chr_to_word, word_to_chr = {}, {}
        for i in range(n):
            a_word, a_chr = words[i], pattern[i]
            # if a char has not visited, corrensponding word must also be not visited(or return False).
            if a_chr not in chr_to_word:
                if a_word in word_to_chr: return False
                # Put that pair in
                chr_to_word[a_chr], word_to_chr[a_word] = a_word, a_chr
            # If a char has visited dict[a_chr] must equal to a_word, and dict[a_word] must equal to a_chr
            else:
                if chr_to_word[a_chr] != a_word or a_word not in word_to_chr or word_to_chr[a_word] != a_chr:
                    return False
                # If valid, do nothing. Keep looping
        return True
sol = Solution()
print sol.("abba", "dog cat cat dog")
print sol.("abba", "dog cat cat fish")
print sol.("abba", "dog cat cat dog")
print sol.("abba", "dog dog dog dog")