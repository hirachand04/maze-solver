"""
SolverBFS: Breadth-First Search maze solver
"""
from collections import deque


class SolverBFS:
    def __init__(self, maze, start, end):
        """
        Initialize BFS solver. 
        
        Args:
            maze (list): 2D grid (0=wall, 1=path)
            start (list): [row, col] starting position
            end (list): [row, col] ending position
        """
        self.maze = maze
        self.start = tuple(start)
        self.end = tuple(end)
        self.rows = len(maze)
        self.cols = len(maze[0]) if maze else 0
        
    def solve(self):
        """
        Solve maze using BFS. 
        
        Returns:
            dict: Visited cells, solution path, and step count
        """
        queue = deque([self.start])
        visited = {self.start: None}
        visited_order = [list(self.start)]
        
        # Directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        while queue:
            current = queue.popleft()
            
            # Check if we reached the end
            if current == self.end:
                path = self._reconstruct_path(visited)
                return {
                    'method': 'bfs',
                    'visited': visited_order,
                    'path': path,
                    'steps': len(visited_order)
                }
            
            # Explore neighbors
            for dr, dc in directions:
                neighbor = (current[0] + dr, current[1] + dc)
                
                if self._is_valid(neighbor) and neighbor not in visited:
                    visited[neighbor] = current
                    visited_order.append(list(neighbor))
                    queue.append(neighbor)
        
        # No solution found
        return {
            'method': 'bfs',
            'visited': visited_order,
            'path': [],
            'steps': len(visited_order)
        }
    
    def _is_valid(self, pos):
        """Check if position is valid and walkable."""
        row, col = pos
        return (0 <= row < self.rows and 
                0 <= col < self.cols and 
                self.maze[row][col] == 1)
    
    def _reconstruct_path(self, visited):
        """Reconstruct path from start to end."""
        path = []
        current = self.end
        
        while current is not None:
            path.append(list(current))
            current = visited[current]
        
        path.reverse()
        return path