from .node import Node
import numpy as np

class BinaryOperation(Node):
    def __init__(self, parent1, parent2):
        """
        Initializes a Plus node that adds to inputs together.

        Args:
            parent1 (_type_, optional): _description_. Defaults to None.
            parent2 (_type_, optional): _description_. Defaults to None.
        """
        self.parents = [parent1, parent2]
        
        
class UnaryOperation(Node):
    def __init__(self, parent):
        self.parents = [parent]


class Plus(BinaryOperation):
    def get_output_shape(self):
        """
        Since the parent shapes should be the same, we can return the first one.

        Returns:
            Tuple[int]: the original shape of a parent
        """
        return self.parents[0].get_output_shape()
    
    def check_if_parents_valid(self):
        return self.parents[0].get_output_shape() == self.parents[1].get_output_shape()
    
    def __str__(self) -> str:
        return f'{self.parents[0]} + {self.parents[1]}'
    

class MultiplyElementWise(BinaryOperation):
    def get_output_shape(self):
        return self.parents[0].get_output_shape()
    
    def check_if_parents_valid(self):
        """
        Check that the second parent is a scalar.
        """
        return self.parents[1].get_output_shape() == (1,)
    
    def __str__(self) -> str:
        return f'Multiply {self.parents[0]} by scalar {self.parents[1]}'
    

class ReLU(UnaryOperation):
    def get_output_shape(self):
        return self.parents[0].get_output_shape()
    
    def check_if_parents_valid(self):
        return True
    
    def __str__(self) -> str:
        return f'ReLU on input of shape {self.get_output_shape()}'
    
class Flatten(UnaryOperation):
    def get_output_shape(self):
        parent_shape = self.parents[0].get_output_shape()
        if len(parent_shape) >= 2:
            return (parent_shape[0], np.prod(parent_shape[1:]))
        else:
            return parent_shape
