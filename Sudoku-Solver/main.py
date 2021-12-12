
import copy  # to make a deepcopy of the board
from typing import List, Any, Tuple
from board import Board
from queue import Queue
from stack import Stack

# Work on DFS and BFS here
def DFS(state: Board) -> Board:
    """Performs a depth first search. Takes a Board and attempts to assign values to
    most constrained cells until a solution is reached or a mistake has been made at
    which point it backtracks.
    Args:
    state - an instance of the Board class to solve, need to find most constrained
      cell and attempt an assignment
    Returns:
    either None in the case of invalid input or a solved board
    """
  

    stack = Stack()
    stack.push(state)
    while(not stack.is_empty()):
        current_state = stack.pop()
        if current_state.goal_test():
            return current_state
        elif not current_state.failure_test():
            row, col = current_state.find_most_constrained_cell()
            for placement in current_state.rows[row][col]:
                b = copy.deepcopy(current_state)
                #print(str(row) + " " + str(col) + " " + str(current_state.rows[row][col])) 
                b.update(row, col, placement)
                stack.push(b)
        else:
            pass
          
                
    return None
            
        
      
  
  


def BFS(state: Board) -> Board:
    """Performs a breadth first search. Takes a Board and attempts to assign values to
    most constrained cells until a solution is reached or a mistake has been made at
    which point it backtracks.
    Args:
    state - an instance of the Board class to solve, need to find most constrained
      cell and attempt an assignment
    Returns:
    either None in the case of invalid input or a solved board
    """
    
    queue = Queue()
    queue.push(state)
    while(not queue.is_empty()):
        current_state = queue.pop()
        if current_state.goal_test():
            return current_state
        elif not current_state.failure_test():
            row, col = current_state.find_most_constrained_cell()
            for placement in current_state.rows[row][col]:
                b = copy.deepcopy(current_state) 
                #print(str(row) + " " + str(col) + " " + str(current_state.rows[row][col])) 
                b.update(row, col, placement)
                queue.push(b)
        else:
            pass
          
    return None


# Function for testing dfs and bfs
def test_dfs_or_bfs(use_dfs: bool, moves: List[Tuple[int, int, int]]) -> None:
    b = Board()
    # make initial moves to set up board
    for move in moves:
        b.update(*move)

    # print initial board
    print("<<<<< Initial Board >>>>>")
    b.print_pretty()
    # solve board
    solution = (DFS if use_dfs else BFS)(b)
    # print solved board
    print("<<<<< Solved Board >>>>>")
    solution.print_pretty()

# sets of moves for the different games
first_moves = [
    (0, 1, 7),
    (0, 7, 1),
    (1, 2, 9),
    (1, 3, 7),
    (1, 5, 4),
    (1, 6, 2),
    (2, 2, 8),
    (2, 3, 9),
    (2, 6, 3),
    (3, 1, 4),
    (3, 2, 3),
    (3, 4, 6),
    (4, 1, 9),
    (4, 3, 1),
    (4, 5, 8),
    (4, 7, 7),
    (5, 4, 2),
    (5, 6, 1),
    (5, 7, 5),
    (6, 2, 4),
    (6, 5, 5),
    (6, 6, 7),
    (7, 2, 7),
    (7, 3, 4),
    (7, 5, 1),
    (7, 6, 9),
    (8, 1, 3),
    (8, 7, 8),
]

second_moves = [
    (0, 1, 2),
    (0, 3, 3),
    (0, 5, 5),
    (0, 7, 4),
    (1, 6, 9),
    (2, 1, 7),
    (2, 4, 4),
    (2, 7, 8),
    (3, 0, 1),
    (3, 2, 7),
    (3, 5, 9),
    (3, 8, 2),
    (4, 1, 9),
    (4, 4, 3),
    (4, 7, 6),
    (5, 0, 6),
    (5, 3, 7),
    (5, 6, 5),
    (5, 8, 8),
    (6, 1, 1),
    (6, 4, 9),
    (6, 7, 2),
    (7, 2, 6),
    (8, 1, 4),
    (8, 3, 8),
    (8, 5, 7),
    (8, 7, 5),
]

print("<<<<<<<<<<<<<< Testing DFS on First Game >>>>>>>>>>>>>>")

test_dfs_or_bfs(True, first_moves)

print("<<<<<<<<<<<<<< Testing DFS on Second Game >>>>>>>>>>>>>>")

test_dfs_or_bfs(True, second_moves)

print("<<<<<<<<<<<<<< Testing BFS on First Game >>>>>>>>>>>>>>")

test_dfs_or_bfs(False, first_moves)

print("<<<<<<<<<<<<<< Testing BFS on Second Game >>>>>>>>>>>>>>")

test_dfs_or_bfs(False, second_moves)
pass
