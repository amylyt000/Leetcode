class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def remove_all(list, val):
            return [value for value in list if value != val]


        for i in range(len(board)):
            vector = board[i]
            vector = remove_all(vector, '.')
            if len(vector) != len(set(vector)):
                # print("a")
                return False

        # print(board)
        for i in range(len(board)):
            # print("b", i)
            vector = []
            for j in range(len(board)):
                    vector.append(board[j][i])
            # print(vector)

            vector = remove_all(vector, '.')
            if len(vector) != len(set(vector)):
                
                # print(vector)
                return False

        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                vector = []
                for k in range(3):
                    for l in range(3):
                        vector.append(board[i+k][j+l])


                vector = remove_all(vector, '.')
                if len(vector) != len(set(vector)):
                    # print("c")
                    return False 

        return True

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(Solution().isValidSudoku(board))




