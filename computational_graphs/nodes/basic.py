from .node import Node
import numpy as np

class Value(Node):
    def __init__(self, value):
        """
        Initializes a Plus node that adds to inputs together.

        Args:
            parent1 (_type_, optional): _description_. Defaults to None.
            parent2 (_type_, optional): _description_. Defaults to None.
        """
        self.value = value
        self.parents = [None]
    
    def check_if_parents_valid(self):
        """
        For addition, the parent's shapes must be the same.

        Returns:
            bool: if the parent's shapes are the same.
        """
        return True
    
    def get_output_shape(self):
        """
        Since the parent shapes should be the same, we can return the first one.

        Returns:
            Tuple[int]: the original shape of a parent
        """
        return self.value.shape
    
    def __str__(self) -> str:
        return f'Value of size {self.get_output_shape()}'