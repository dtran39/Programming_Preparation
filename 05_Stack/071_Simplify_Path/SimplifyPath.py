class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack, tokens = [], path.split('/')
        for a_token in tokens:
            # If encounter .. and already inside a folder (stack has element) -> don't need to go that way
            # -> pop stack
            if a_token == '..':
                if stack:
                    stack.pop()
            # Encounter . skip/do nothing
            elif a_token == '.':
                continue
            # Otherwise a token must not be empty
            elif a_token:
                stack.append(a_token)
        return '/' + '/'.join(stack)