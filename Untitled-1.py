class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        # Convert rows to tuples for hashing
        rows = [tuple(row) for row in grid]
        row_counts = {}
        
        # Count occurrences of each row
        for row in rows:
            row_counts[row] = row_counts.get(row, 0) + 1
            print(row_counts.get(row, 0))
        
        # Convert columns to tuples for hashing
        columns = [tuple(col) for col in zip(*grid)]
        
        # Count matches between rows and columns
        counter = 0
        for col in columns:
            counter += row_counts.get(col, 0)
            print(row_counts.get(col, 0))
        
        return counter
a = Solution()
print(a.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))