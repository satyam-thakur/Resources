class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        n = 3
        rows, cols = [0] * n, [0] * n
        diag1 = diag2 = 0
        player = 1
        for r, c in moves:
            rows[r]+=player
            cols[c]+=player
            if r==c: diag1 += player
            if r+c==n-1: diag2 += player
            if abs(rows[r])==n or abs(cols[c])==n or abs(diag1)==n or abs(diag2)==n:
                if player == 1:
                    return 'A'
                else:
                    return 'B'
            player*=-1

        if len(moves)==n*n:
            return "Draw"
        else:
            return "Pending"
        
print (Solution.tictactoe(None,[[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))

#https://www.youtube.com/watch?v=vNQdejhNyT0
