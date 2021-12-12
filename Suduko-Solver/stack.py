from typing import Generic, List, TypeVar

# stack element type variable
S = TypeVar("S")

class Stack:
  """A last in first out (LIFO) stack representation where elements are pushed and
  popped from the top. Think of a stack of plates, where you can't remove or add a
  plate in the middle, only take from, or add to, the top
  Attributes:
    the_stack - the list that holds the elements of our stack
  """

  def __init__(self, initial: List[S] = []) -> None:
    """Constructor for a stack, set the stack up with the given list if any is
    provided otherwise empty
    Args:
      initial - optional list of elements to fill the stack with
    """

    # can't have lists (mutable objects in general) as default values as the default
    # is shared among all instances. need to copy here to avoid issues with aliases
    self.the_stack: List[S] = initial[:]

  def __str__(self) -> str:
    """String representation of the stack"""
    return f"The stack contains: {self.the_stack}"

  def is_empty(self) -> bool:
    """Check if stack has no elements
    Returns:
      True if stack has no elements, False otherwise
    """
    return len(self.the_stack) == 0

  def push(self, elt: S) -> None:
    """Add element (elt) to top of stack
    Args:
      elt - an item to add to the stack
    """
    self.the_stack.append(elt)

  def pop(self) -> S:
    """Remove and return the top item in the stack (corresponds to the last item in
    the list)
    Returns:
      the most recently added element
    """
    return self.the_stack.pop()
