from .node import Node

class Plus(Node):
    def __init__(self, parent1 = None, parent2 = None):
        """
        Initializes a Plus node that adds to inputs together.

        Args:
            parent1 (_type_, optional): _description_. Defaults to None.
            parent2 (_type_, optional): _description_. Defaults to None.
        """
        self.parents = [parent1, parent2]
    
    def check_if_parents_valid(self):
        """
        For addition, the parent's shapes must be the same.

        Returns:
            bool: if the parent's shapes are the same.
        """
        return self.parents[0] == self.parents[1]
    
    def get_output_shape(self):
        """
        Since the parent shapes should be the same, we can return the first one.

        Returns:
            Tuple[int]: the original shape of a parent
        """
        return self.parents[0]