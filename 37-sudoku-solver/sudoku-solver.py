class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Step 1: Pre-populate existing numbers and track empty cells
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty_cells.append((r, c))
                else:
                    box_idx = (r // 3) * 3 + (c // 3)
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)

        # Step 2: Backtrack only through empty cells
        def backtrack(index: int) -> bool:
            if index == len(empty_cells):
                return True  # All empty cells filled successfully
            
            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + (c // 3)

            for digit in '123456789':
                if digit not in rows[r] and digit not in cols[c] and digit not in boxes[box_idx]:
                    # Place digit and update tracking sets
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box_idx].add(digit)

                    if backtrack(index + 1):
                        return True

                    # Undo placement (Backtrack)
                    board[r][c] = '.'
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[box_idx].remove(digit)

            return False

        backtrack(0)