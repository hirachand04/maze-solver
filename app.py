"""
Flask API for Maze Generator and Solver
"""
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from maze_generator import MazeGenerator
from solver_bfs import SolverBFS
from solver_dfs import SolverDFS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    """Redirect to maze visualizer."""
    return send_from_directory('static', 'maze.html')


@app.route('/static/<path:path>')
def serve_static(path):
    """Serve static files."""
    return send_from_directory('static', path)


@app.route('/generate', methods=['GET'])
def generate_maze():
    """
    Generate a new maze.
    
    Query Parameters:
        rows (int): Number of rows (default: 20)
        cols (int): Number of columns (default: 20)
    
    Returns:
        JSON with maze data
    """
    try:
        rows = int(request.args.get('rows', 20))
        cols = int(request.args.get('cols', 20))
        
        # Validate dimensions
        if rows < 5 or cols < 5:
            return jsonify({'error': 'Minimum size is 5x5'}), 400
        if rows > 100 or cols > 100:
            return jsonify({'error': 'Maximum size is 100x100'}), 400
        
        # Ensure odd dimensions for proper maze generation
        if rows % 2 == 0:
            rows += 1
        if cols % 2 == 0:
            cols += 1
        
        generator = MazeGenerator(rows, cols)
        maze_data = generator.generate()
        
        return jsonify(maze_data)
    
    except ValueError:
        return jsonify({'error': 'Invalid parameters'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/solve', methods=['POST'])
def solve_maze():
    """
    Solve a maze using specified algorithm.
    
    Query Parameters:
        method (str): 'bfs' or 'dfs' (default: 'bfs')
    
    Request Body:
        JSON with maze, start, and end
    
    Returns:
        JSON with solution data
    """
    try:
        method = request.args.get('method', 'bfs').lower()
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        maze = data.get('maze')
        start = data.get('start')
        end = data.get('end')
        
        if not maze or not start or not end:
            return jsonify({'error': 'Missing maze, start, or end'}), 400
        
        # Choose solver
        if method == 'bfs':
            solver = SolverBFS(maze, start, end)
        elif method == 'dfs':
            solver = SolverDFS(maze, start, end)
        else:
            return jsonify({'error': 'Invalid method. Use bfs or dfs'}), 400
        
        solution = solver.solve()
        return jsonify(solution)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    print("🚀 Maze Solver API is running!")
    print("📍 Open http://localhost:5000/static/maze.html in your browser")
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
