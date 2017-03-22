'''
Problem:
    -
Implement an iterator to flatten a 2d vector.

For example,
----------------------------------------------------------------------------------------------------
Examples: 
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].
----------------------------------------------------------------------------------------------------
Solution: 
'''
class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.horPtr, self.verPtr = 0, 0
    def next(self):
        val = self.vec2d[self.verPtr][self.horPtr]
        self.horPtr += 1
        return val

    def hasNext(self):
        # Find next available element
        while self.verPtr < len(self.vec2d):
            if self.horPtr < len(self.vec2d[self.verPtr]):
                return True
            self.verPtr += 1
            self.horPtr = 0
        return False
# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())