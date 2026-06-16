# Time Compleixty --> O(m*n)
# Space Compleixty --> O(m*n)
# Approach --> DFS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        if image[sr][sc]==color:
            return image
        self.oldcolor = image[sr][sc]
        self.dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        self.dfs(image, sr, sc, color)
        return image
    
    def dfs(self, image, r, c, color):
        # base
        if r<0 or c<0 or r == len(image) or c == len(image[0]):
            return
        if image[r][c] != self.oldcolor:
            return

        # logic
        image[r][c] = color
        for dir in self.dirs:
            nr = r + dir[0]
            nc = c + dir[1]
            self.dfs(image, nr, nc, color)


'''
# Time Compleixty --> O(m*n)
# Space Compleixty --> O(m*n)
# Approach --> BFS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        oldcolor = image[sr][sc]
        
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        q = deque()
        q.append((sr,sc))
        image[sr][sc] = color
        while len(q)>0:
            curr = q.popleft()
            for dir in dirs:
                nr = curr[0] + dir[0]
                nc = curr[1] + dir[1]
                if nr>=0 and nc>=0 and nr<len(image) and nc<len(image[0]) and image[nr][nc]==oldcolor:
                    q.append((nr,nc))
                    image[nr][nc] = color 
        return image 


'''
