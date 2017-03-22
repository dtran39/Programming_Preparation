def count(s):
    stack = []
    count = 0
    sym = {'(': ')', '{': '}', '[': ']'}
    for i in range(len(s)):
        if s[i] in ['(', '[', '{']:
            stack.append(i)
        else:
            if not stack or s[i] != sym[stack[-1]]:
                continue
            
print count("(){](({}))[]")
