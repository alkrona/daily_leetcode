def exist(board,word):
    m,n = len(board),len(board[0])
    for i in range(m):
        for j in range(n):
            if dfs(i,j,board,word):return True
    return False

def dfs(i,j,board,word,k=0):
    if k==len(word): return True
    m,n = len(board),len(board[0])
    if not (0<=i<m and 0<=j<n): return False
    if board[i][j]!=word[k]:return False
    board[i][j]="?"
    if(dfs(i+1,j,board,word,k+1) or dfs(i-1,j,board,word,k+1) or dfs(i,j+1,board,word,k+1) or dfs(i,j-1,board,word,k+1) ): return True
    board[i][j] = word[k]
if __name__=="__main__":
    print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"))
