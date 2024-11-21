class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Step 1: Initialize the boundaries of the matrix
        # Boundaries define karte hain: top, bottom, left, right
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        result = []  # Ye list humara final spiral order store karega

        # Step 2: Loop until all boundaries overlap or cross
        while top <= bottom and left <= right:
            # Move from left to right along the top row
            # Top row se left to right traverse karte hain
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # Top boundary ko neeche move karte hain

            # Move from top to bottom along the right column
            # Right column se top to bottom traverse karte hain
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # Right boundary ko left ki taraf move karte hain

            # Check if there are still rows remaining
            # Agar rows abhi bhi bachi hain, toh left to right traverse karenge
            if top <= bottom:
                # Move from right to left along the bottom row
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # Bottom boundary ko upar move karte hain

            # Check if there are still columns remaining
            # Agar columns abhi bhi bachi hain, toh bottom to top traverse karenge
            if left <= right:
                # Move from bottom to top along the left column
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Left boundary ko right ki taraf move karte hain

        return result  # Yeh final spiral order return karta hai
