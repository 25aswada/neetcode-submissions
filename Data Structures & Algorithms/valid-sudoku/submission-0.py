class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    val = board[i][j]
                    box_index = (i // 3) * 3 + (j // 3)

                    if val in rows[i] or val in cols[j] or val in boxes[box_index]:
                        return False

                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[box_index].add(val)

        return True