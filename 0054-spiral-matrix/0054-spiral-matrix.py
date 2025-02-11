class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:  # Edge case: empty matrix
            return []

        order = []
        top, left = 0, 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Move Right →
            for c in range(left, right + 1):
                order.append(matrix[top][c])
            top += 1  # Move top boundary down

            # Move Down ↓
            for r in range(top, bottom + 1):
                order.append(matrix[r][right])
            right -= 1  # Move right boundary left

            # Move Left ← (Check if row still exists)
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    order.append(matrix[bottom][c])
                bottom -= 1  # Move bottom boundary up

            # Move Up ↑ (Check if column still exists)
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    order.append(matrix[r][left])
                left += 1  # Move left boundary right

        return order
