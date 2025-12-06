# 🌀 Maze Generator and Solver

A complete Python-based maze generation and solving system with an interactive web visualization.  Generate random mazes using DFS-based algorithms and solve them using BFS or DFS with step-by-step animation.

## ✨ Features

- **Maze Generation**: DFS-based recursive backtracking algorithm
- **Dual Solving Algorithms**: 
  - Breadth-First Search (BFS) - guarantees shortest path
  - Depth-First Search (DFS) - explores depth-first
- **REST API**: Flask-based API with JSON endpoints
- **Interactive Visualizer**: Animated solving process with customizable speed
- **Modular Architecture**: Clean, object-oriented Python code

## 🎯 Project Structure

```
maze-solver/
├── app.py                 # Flask API server
├── maze_generator.py      # MazeGenerator class
├── solver_bfs.py          # BFS solver class
├── solver_dfs. py          # DFS solver class
├── static/
│   └── maze.html          # Frontend visualizer
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hirachand04/maze-solver.git
   cd maze-solver
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🏃 Running the Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:5000/static/maze. html
   ```

3. **Use the visualizer**:
   - Click **"Generate Maze"** to create a new random maze
   - Adjust rows and columns for different maze sizes
   - Click **"Solve (BFS)"** or **"Solve (DFS)"** to visualize solving
   - Use the **speed slider** to control animation speed
   - Click **"Reset"** to clear the solution

## 📡 API Endpoints

### Generate Maze
```
GET /generate? rows=20&cols=20
```

**Parameters**:
- `rows` (optional): Number of rows (default: 20, range: 5-100)
- `cols` (optional): Number of columns (default: 20, range: 5-100)

**Response**:
```json
{
  "maze": [[0,1,0,... ], ... ],
  "rows": 20,
  "cols": 20,
  "start": [1, 1],
  "end": [18, 18]
}
```

### Solve Maze
```
POST /solve? method=bfs
```

**Parameters**:
- `method` (optional): Solving algorithm - `bfs` or `dfs` (default: `bfs`)

**Request Body**:
```json
{
  "maze": [[0,1,0,...], ...],
  "start": [1, 1],
  "end": [18, 18],
  "rows": 20,
  "cols": 20
}
```

**Response**:
```json
{
  "method": "bfs",
  "visited": [[1,1], [1,2], ... ],
  "path": [[1,1], [2,1], .. ., [18,18]],
  "steps": 156
}
```

## 🧠 Algorithms

### Maze Generation (DFS)
Uses **recursive backtracking** to create perfect mazes:
1. Start from a random cell
2. Mark it as part of the maze
3. Randomly choose an unvisited neighbor
4.  Carve a path to that neighbor
5. Recursively repeat from the neighbor
6. Backtrack when no unvisited neighbors remain

### Breadth-First Search (BFS)
- Uses a **queue** (FIFO)
- Explores level-by-level
- **Guarantees shortest path**
- More memory intensive

### Depth-First Search (DFS)
- Uses a **stack** (LIFO)
- Explores one path deeply before backtracking
- May not find shortest path
- More memory efficient

## 🎨 Visualization Color Scheme

- **Black** (#000000): Walls
- **White** (#FFFFFF): Walkable paths
- **Blue** (#4A90E2): Visited cells during solving
- **Green** (#00FF00): Final solution path
- **Dark Green**: Start position
- **Dark Red**: End position

## 🛠️ Architecture

### Backend Classes

**MazeGenerator**
- Generates random mazes using DFS
- Configurable dimensions
- Ensures solvable mazes

**SolverBFS**
- Implements breadth-first search
- Tracks visited order
- Reconstructs optimal path

**SolverDFS**
- Implements depth-first search
- Tracks visited order
- Finds valid path (may not be shortest)

### Frontend
- Vanilla JavaScript (no frameworks)
- HTML5 Canvas for rendering
- Responsive design
- Smooth animations

## 📝 Example Usage

```python
from maze_generator import MazeGenerator
from solver_bfs import SolverBFS

# Generate a maze
generator = MazeGenerator(21, 21)
maze_data = generator.generate()

# Solve with BFS
solver = SolverBFS(maze_data['maze'], maze_data['start'], maze_data['end'])
solution = solver.solve()

print(f"Path length: {len(solution['path'])}")
print(f"Cells visited: {solution['steps']}")
```

## 🧪 Testing

Test different maze sizes:
```bash
# Small maze
curl "http://localhost:5000/generate?rows=5&cols=5"

# Medium maze
curl "http://localhost:5000/generate?rows=25&cols=25"

# Large maze
curl "http://localhost:5000/generate?rows=51&cols=51"
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📄 License

MIT License - feel free to use this project for learning and development. 

## 👤 Author

**hirachand04**

---

**Enjoy exploring mazes!** 🎉"# maze-solver" 
