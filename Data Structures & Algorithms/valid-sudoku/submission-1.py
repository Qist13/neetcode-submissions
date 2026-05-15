class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_map = {
            "rows": [[] for _ in range(9)],
            "cols": [[] for _ in range(9)],
            "boxes": [[] for _ in range(9)]
        }

        for i in range(len(board)):
            hash_map["rows"][i] = board[i]
            for j in range(len(board[i])):
                hash_map["cols"][j].append(board[i][j])
                box = (i // 3) * 3 + (j // 3)
                hash_map["boxes"][box].append(board[i][j])

        for item in hash_map.values():
            for arr in item:
                if not self.isNoDupes(arr):
                    return False
        
        return True

    def isNoDupes(self, arr: List[str]) -> bool:
        hash_set = set()

        for s in arr:
            if not s == '.':
                if int(s) in hash_set:
                    return False
                else:
                    hash_set.add(int(s))
        
        return True
    