class Solution:
    # Time O(N*M) | Space O(N)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        left = 0
        right = len(matrix[0])

        top = 0
        bottom = len(matrix)

        while left < right and top < bottom:
            # for each top row value
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # for each right col value
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1

            # check for break
            if not (left < right and top < bottom):
                break

            # for each bottom col value
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            # for each left col value
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1

        return res
