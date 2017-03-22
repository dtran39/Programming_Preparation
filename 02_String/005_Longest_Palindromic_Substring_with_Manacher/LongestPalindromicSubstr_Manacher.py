'''
Problem:
    - Find longest palindromic substring
----------------------------------------------------------------------------------------------------
Examples: 
"abaxabaxabb"                       "baxabaxab"
"forgeeksskeegfor",                 "geeksskeeg"
"abaabac"                           "abaaba"
"abaaba"                            "abaaba"
"abababa"                           "abababa"
"ababac"                            "ababa"
"abcbabcbabcba",                    "abcbabcbabcba"
----------------------------------------------------------------------------------------------------
Solution: 
    https://www.akalin.com/longest-palindrome-linear-time

Manacher:
    - An optimization from the center expansion problem
    - Key: How to pick the next center after expanding the last center
        TAKE THE CENTER OF THE LONGEST PALINDROMIC PROPER SUFFIX OF THE CURRENT PALINDROME
        Why: Because it's at least a long palindrome, and we can expand it further
        Fact 1: a palindromic proper suffix of a palindrome has 
            a corresponding dual palindromic proper prefix. 
            Ex: abcbabcba: lpps is "abcba". also there will be a "abcba" in the front
        Fact 2: we don't have to keep track of all the palindromes we've seen
            Ex: abcbabcba, we don't care about "bcb" since it contained in "abcba"
        1. Fill in the LPS of the leftmost position, the one just before the first character; 
            it's the empty string, of course (length zero). 
            Then start at the first character of the string; 
                this will be the first position we visit.
        2. Find the LPS centered at the current position by 
            scanning backward and forward and stopping when 
                we hit one of the ends of the string
                or we find two characters that differ. 
            Record the length of the LPS. 
            If the current position is after the last character of the string:
                halt; we're done.
        3. Find the longest palindromic suffix of the LPS centered at the current position 
            by scanning backward and looking for the longest palindromic prefix. 
            That is, scan until you find a position such that 
                the first character of the LPS at that position is either 
                    the first character of the LPS at the current position, 
                    or to the left of it. 
            Along the way, reflect the LPS lengths across the current position, 
                thus recording the lengths of the LPSes centered at positions 
                to the left of the centre of the longest palindromic suffix.
        4. Set the current position to the position of the longest palindromic suffix 
            (the reflection of the centre of the longest palindromic prefix across the current position). 
            Go back to step 2.
Tushar: 
    - Idea: Optimize from expansion solution 
        + It doesn't reused the palindromic property from previous substr, so the complexity is O(n ^ 2)
    - In LPS Array L:
        LPS length value at odd positions (the actual character positions) 
            will be odd and greater than or equal to 1 (at least the character)
        LPS length value at even positions (the positions between two characters, left of first and right of last chars)
            will be even and greater than or equal to 0
    - Index: from 0 to n - 1.   Position: from 0 to 2n
    -  if there is a palindrome in a string centered at some position, 
        then LPS length values around the center position may or may not be symmetric 
        depending on some situation. 
    -> If we can know when the values are symmetric, we will avoid repetitive calculation -> Reduce time to linear
    - 4 cases:
     * Case 1 : 
        Right side palindrome is totally contained under current palindrome. 
            In this case do not consider this as center.
     * Case 2 : 
        Current palindrome is proper suffix of input. 
            Terminate the loop in this case. No better palindrom will be found on right.
     * Case 3 : 
        Right side palindrome is proper suffix and 
        its corresponding left side palindrome is proper prefix of current palindrome. 
            Make largest such point as next center.
     * Case 4 : 
        Right side palindrome is proper suffix but 
        its left corresponding palindrome is be beyond current palindrome. 
            Do not consider this as center because it will not extend at all.

----------------------------------------------------------------------------------------------------
'''
# Python program to implement Manacher's Algorithm
def find_lps(s):
    # Preprocess input (create char array with dummy character) 
        #to handle even length palindrome case
    # Must reask if the string only has alphanumeric character
    str_len = len(s)
    num_chrs = 2 * str_len + 1
    chr_list = []
    s_ptr = 0
    for i in range(num_chrs):
        if i % 2 != 0: 
            chr_list.append(s[s_ptr])
            s_ptr += 1
        else: chr_list.append('$')
    # Array to hold length of lps at each point
    max_lps = [0] * num_chrs
    start, end, i = 0, 0, 0
    while i < num_chrs:
        while start > 0 and end < num_chrs - 1 and chr_list[start - 1] == chr_list[end + 1]:
            start, end = start - 1, end + 1
        max_lps[i] = end - start + 1
        # if current palindrome is proper suffix of input (case 2), 
            #then there is nothing to explore -> break
        if end == num_chrs - 1: break
        # Make new center = end (if i is odd, then new center = end + 1)
        new_center = end
        if i % 2 == 0: new_center += 1
        # 
        for j in range(i + 1, end + 1):
            left_mirror_ptr = i - (j - i)
            # In case left mirror might go beyond current center palindrome
            max_lps[j] = min(max_lps[left_mirror_ptr], 2 * (end - j) + 1)
            #Only proceed if we get case 3. 
                # This check is to make sure we do not pick j as new center for 
                    #case 1 (right side is contained under current palindrome)
                    #case 4 (right side is properf suffix, but left side goes beyond)
                    # In general, when length of palindrome on left side is still bigger
                # As soon as we find a center (case 3 match: right side is suffix and left side is prefix) 
                    #lets break out of this inner while loop.
            if j + max_lps[left_mirror_ptr] / 2 == end:
                new_center = j
                break
        i = new_center
        #  Set right and left to at least the value 
            #we already know should be matching based of left side palindrome.
        end = i + max_lps[i]/2
        start = i - max_lps[i]/2
    # //find the max palindrome in T and return it.
    start, end, global_max_lps = -1, -1, -1
    for i in range(num_chrs):
        cur_max_lps = max_lps[i]
        if cur_max_lps > global_max_lps:
            global_max_lps = cur_max_lps
            start, end = i - cur_max_lps / 2, i + cur_max_lps / 2
    return s[start / 2 :  end / 2]
print find_lps("abaxabaxabb")
print find_lps("forgeeksskeegfor")
print find_lps("abaabac")
print find_lps("abaaba")
print find_lps("abababa")
print find_lps("ababac")
# print find_lps("abcbabcbabcba")