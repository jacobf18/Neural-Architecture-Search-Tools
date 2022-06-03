from .node import Node

class BinaryOperation(Node):
    def __init__(self, parent1 = None, parent2 = None):
        """
        Initializes a Plus node that adds to inputs together.

        Args:
            parent1 (_type_, optional): _description_. Defaults to None.
            parent2 (_type_, optional): _description_. Defaults to None.
        """
        self.parents = [parent1, parent2]
        
        
class UnaryOperation(Node):
    def __init__(self, parent=None):
        self.parents = [parent]


class Plus(BinaryOperation):
    def get_output_shape(self):
        """
        Since the parent shapes should be the same, we can return the first one.

        Returns:
            Tuple[int]: the original shape of a parent
        """
        return self.parents[0]
    
    def check_if_parents_valid(self):
        return self.parents[0].get_output_shape() == self.parents[1].get_output_shape()
    
    def __str__(self) -> str:
        return f'{self.parents[0]} + {self.parents[1]}'
    
class Multiply(BinaryOperation):
    pass
