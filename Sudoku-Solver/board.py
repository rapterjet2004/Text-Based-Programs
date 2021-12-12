import copy  # to make a deepcopy of the board
from typing import List, Any, Tuple

# HELPER FUNCTION TO REMOVE ITEMS FROM A LIST
def remove_if_exists(lst: Any, elem: Any) -> None:
  """Takes a list and element and removes that element if it exists in the list
  Args:
    lst - the list you're trying to remove an item from
    elem - item to remove
  """
  if isinstance(lst, list) and elem in lst:
    lst.remove(elem)

class Board:
  """Represents a state (situation) in a Sudoku puzzle. Some cells may have filled in
  numbers while others have not. Cells that have not been filled in hold the potential
  values that could be assigned to the cell (i.e. have not been ruled out from the
  row, column or subgrid)
  Attributes:
    num_nums_placed - number of numbers placed so far (initially 0)
    size - the size of the board (this will always be 9, but is convenient to have
      an attribute for this for debugging purposes)
    rows - a list of 9 lists, each with 9 elements (imagine a 9x9 sudoku board).
      Each element will itself be a list of the numbers that remain possible to
      assign in that square. Initially, each element will contain a list of the
      numbers 1 through 9 (so a triply nested 9x9x9 list to start) as all numbers
      are possible when no assignments have been made. When an assignment is made
      this innermost element won't be a list of possibilities anymore but the
      single number that is the assignment.
  """

  def __init__(self):
    """Constructor for a board, sets up a board with each element having all
    numbers as possibilities"""
    self.size: int = 9
    self.num_nums_placed: int = 0

    # triply nested lists, representing a 9x9 sudoku board
    # 9 quadrants, 9 cells in each 3*3 subgrid, 9 possible numbers in each cell
    # Note: using Any in the type hint since the cell can be either a list (when it
    # has not yet been assigned a value) or a value (once it has been assigned)
    # Note II: a lone underscore is a common convention for unused variables
    self.rows: List[List[Any]] = (
      [[list(range(1, 10)) for _ in range(self.size)] for _ in range(self.size)]
    )

  def __str__(self) -> str:
    """String representation of the board"""
    row_str = ""
    for r in self.rows:
      row_str += f"{r}\n"

    return f"num_nums_placed: {self.num_nums_placed}\nboard (rows): \n{row_str}"

  def print_pretty(self):
    """Prints all numbers assigned to cells, excluding lists of possible numbers
    that can still be assigned to cells"""
    row_str = ""
    for i, r in enumerate(self.rows):
      if not i % 3:
        row_str += " -------------------------\n"

      for j, x in enumerate(r):
        row_str += " | " if not j % 3 else " "
        row_str += "*" if isinstance(x, list) else f"{x}"

      row_str += " |\n"

    row_str += " -------------------------\n"
    print(f"num_nums_placed: {self.num_nums_placed}\nboard (rows): \n{row_str}")

  def subgrid_coordinates(self, row: int, col: int) -> List[Tuple[int, int]]:
    """Get all coordinates of cells in a given cell's subgrid (3x3 space)
    Integer divide to get column & row indices of subgrid then take all combinations
    of cell indices with the row/column indices from those subgrids (also known as
    the outer or Cartesian product)
    Args:
      row - index of the cell's row, 0 - 8
      col - index of the cell's col, 0 - 8
    Returns:
      list of (row, col) that represent all cells in the box.
    """
    subgrids = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    # Note: row // 3 gives the index of the subgrid for the row index, this is one
    # of 0, 1 or 2, col // 3 gives us the same for the column
    return [(r, c) for c in subgrids[col // 3] for r in subgrids[row // 3]]

  def find_most_constrained_cell(self) -> Tuple[int, int]:
    """Finds the coordinates (row and column indices) of the cell that contains the
    fewest possible values to assign (the shortest list). Note: in the case of ties
    return the coordinates of the first minimum size cell found
    Returns:
      a tuple of row, column index identifying the most constrained cell
    """
    # inititalizes the intial ints, and creates a big empty list. 
    smallestList = [None] * 10
    smallestRow = -1
    smallestCol = -1
    
    for row in range(9):
        for col in range(9):
            element = self.rows[row][col]
            if(type(element) is list):
                if len(element) < len(smallestList):
                    smallestList = element
                    smallestRow = row
                    smallestCol = col
    
    #returns a tuple
    return (smallestRow, smallestCol)
                
            

  def failure_test(self) -> bool:
    """Check if we've failed to correctly fill out the puzzle. If we find a cell
    that contains an [], then we have no more possibilities for the cell but haven't
    assigned it a value so fail.
    Returns:
      True if we have failed to fill out the puzzle, False otherwise
    """
    for row in self.rows:
        for element in row:
            if element == []:
                return True
                
    return False

  def goal_test(self) -> bool:
    """Check if we've completed the puzzle (if we've placed all the numbers).
    Naively checks that we've placed as many numbers as cells on the board
    Returns:
      True if we've placed all numbers, False otherwise
    """
    if(self.num_nums_placed == 81):
        return True
    
    
    return False

  def update(self, row: int, column: int, assignment: int) -> None:
    """Assigns the given value to the cell given by passed in row and column
    coordinates. By assigning we mean set the cell to the value so instead the cell
    being a list of possibities it's just the new assignment value.  Update all
    affected cells (row, column & subgrid) to remove the possibility of assigning
    the given value.
    Args:
      row - index of the row to assign
      column - index of the column to assign
      assignment - value to place at given row, column coordinate
    """
    
    #set a check to make sure that the given variable is a list
    #by default each empty element is a list of 9 possible values 1-9
    element = self.rows[row][column]
    if type(element) is list and assignment in element:
        self.rows[row][column] = assignment
        self.num_nums_placed = self.num_nums_placed + 1
    
    #Remove the possibility of assigning that value to all affected cells(row, col, & subgrid)
    
    # sub_coord is a list of all cells in the subgrid(the 3x3 box) of the given row, column pair
    sub_coords = self.subgrid_coordinates(row, column)
    
    # iterate through all in subgrids
    for tupl in sub_coords:
        r = tupl[0]
        c = tupl[1]
        element = self.rows[r][c]
        if type(element) is list:
            remove_if_exists(element, assignment)
        
    # iterates through columns
    for i in range(0, 9):
        element = self.rows[i][column]
        if type(element) is list:
            remove_if_exists(element, assignment)
        
        
    # iterates through rows
    for i in range(0,9):
        element = self.rows[row][i]
        if type(element) is list:
            remove_if_exists(element, assignment)
