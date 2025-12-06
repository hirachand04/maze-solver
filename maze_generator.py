"""
MazeGenerator: DFS-based maze generation
"""
import random


class MazeGenerator:
    def __init__(self, rows, cols):
        """
        Initialize maze generator with dimensions. 
        
        Args:
            rows (int): Number of rows
            cols (int): Number of columns
        """
        self.rows = rows
        self.cols = cols
        self.maze = [[0 for _ in range(cols)] for _ in range(rows)]
        
    def generate(self):
        """
        Generate maze using recursive backtracking (DFS).
        
        Returns:
            dict: Maze data with grid, start, and end positions
        """
        # Start from (1, 1) to ensure borders are walls
        start_row, start_col = 1, 1
        self.maze[start_row][start_col] = 1
        self._carve_passages(start_row, start_col)
        
        # Ensure start and end points are accessible
        self.maze[1][1] = 1  # Start point
        self.maze[self.rows - 2][self.cols - 2] = 1  # End point
        
        return {
            'maze': self.maze,
            'rows': self.rows,
            'cols': self.cols,
            'start': [1, 1],
            'end': [self.rows - 2, self.cols - 2]
        }
    
    def _carve_passages(self, row, col):
        """
        Recursively carve passages using DFS.
        
        Args:
            row (int): Current row
            col (int): Current column
        """
        # Directions: up, right, down, left
        directions = [(-2, 0), (0, 2), (2, 0), (0, -2)]
        random.shuffle(directions)
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # Check boundaries
            if (1 <= new_row < self.rows - 1 and 
                1 <= new_col < self.cols - 1 and 
                self.maze[new_row][new_col] == 0):
                
                # Carve passage
                self.maze[new_row][new_col] = 1
                self.maze[row + dr // 2][col + dc // 2] = 1
                
                # Recurse
                self._carve_passages(new_row, new_col)