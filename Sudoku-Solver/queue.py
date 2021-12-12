from typing import Generic, List, TypeVar

# queue element type variable
Q = TypeVar("Q")

class Queue:
  """A first in first out (FIFO) queue representation where elements are pushed at the
  end of the queue and popped from the front. Think of a line at an amusement park
  where new people join (pushed) the line at the back and are let in (popped) from the
  front
  Attributes:
    the_queue - the list that holds the elements of our queue
  """

  def __init__(self, initial: List[Q] = []) -> None:
    """Constructor for a queue, simply sets the queue up with the given list if any
    is provided otherwise empty
    Args:
      initial - optional list of elements to fill the queue with
    """

    # can't have lists (mutable objects in general) as default values as the default
    # is shared among all instances. need to copy here to avoid issues with aliases
    self.the_queue: List[Q] = initial[:]

  def __str__(self) -> str:
    """String representation of the queue"""
    return f"The queue contains: {self.the_queue}"

  def is_empty(self) -> bool:
    """Check if queue has no elements
    Returns:
        True if queue has no elements, False otherwise
    """
    return len(self.the_queue) == 0

  def push(self, elt: Q) -> None:
    """Add element (elt) to end of queue
    Args:
        elt - an item to add to the queue
    """
    self.the_queue.append(elt)

  def pop(self) -> Q:
    """Remove and return the start of the queue (corresponds to the first item in
    the list)
    Returns:
        the oldest added element
    """
    return self.the_queue.pop(0)
