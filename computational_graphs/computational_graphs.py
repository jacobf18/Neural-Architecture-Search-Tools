from abc import ABC, abstractmethod
from typing import List, Tuple
from __future__ import annotations

class Node(ABC):
    """
    Base abstract class which all nodes inherit from.
    """
    parents: List[Node]
    ouput_shape: Tuple[int]
    
    @abstractmethod
    def check_if_parents_valid(self):
        pass
    
    @abstractmethod
    def get_output_shape(self):
        pass

