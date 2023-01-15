class Solution:
    # Time O(N) | Space O(N)
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            # when collision will occur
            while stack and (a < 0) and (stack[-1] > 0):
                diff = stack[-1] + a
                if diff > 0:
                    a = 0
                elif diff < 0:
                    stack.pop()
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)                
        return stack 
