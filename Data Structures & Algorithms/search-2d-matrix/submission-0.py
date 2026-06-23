class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def linearToMatrix(linearIndex: int) -> Tuple[int, int]:
            row = linearIndex // n
            col = linearIndex % n
            return row, col
        
        lo = 0
        hi = m * n - 1
        mid = None
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_row, mid_col = linearToMatrix(mid)
            if matrix[mid_row][mid_col] < target:
                lo = mid + 1
            elif matrix[mid_row][mid_col] == target:
                return True
            else:
                hi = mid - 1
        
        return False