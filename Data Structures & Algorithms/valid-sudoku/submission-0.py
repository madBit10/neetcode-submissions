class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        row_bucket = [set() for _ in range(9)] # row bucket
        col_bucket = [set() for _ in range(9)] # col bucket
        boxes = [set() for _ in range(9)] # box bucket

        for r in range(rows):
            for c in range(cols):
                # checking for the "." char first
                if board[r][c] == ".":
                    continue

                # saving each index in the value variable
                val = board[r][c]
                # checking if the value is already present in the row
                if val in row_bucket[r]:
                    return False
                row_bucket[r].add(val)

                # checking if the value is already present in the column
                if val in col_bucket[c]:
                    return False 
                col_bucket[c].add(val)

                # deducing the box index
                box_index = 3 * (r // 3) + (c // 3)

                # checking if the box index is already present in the boxes bucket
                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)
        
        return True

        