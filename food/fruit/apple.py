from food.fruit.base_fruit import BaseFruit

class Apple(BaseFruit):
    """A class representing an apple fruit.
    """
    def __init__(self, name="Apple", color="red"):
        """Initialize an Apple instance.
        
        Args:
            name (str): The name of the apple variety. Default is "Apple".
            color (str): The color of the apple. Default is "red".
        """
        super().__init__(name, color)

    def make_pie(self, size="medium"):
        """Make an apple pie of a given size.
        
        Args:
            size (str): The size of the pie. Default is "medium".
        """
        print(f"Making {size} apple pie!")

class Fuji(Apple):
    """A class representing a Fuji apple variety.
    """
    def __init__(self, name="Fuji Apple", color="red"):
        """Initialize a Fuji Apple instance.

        Args:
            name (str): The name of the apple variety. Default is "Fuji Apple".
            color (str): The color of the apple. Default is "red".
        """
        super().__init__(name, color)

    def make_cider(self, size="large"):
        """Make Fuji apple cider of a given size.

        Args:
            size (str): The size of the cider. Default is "large".
        """
        print(f"Making {size} Fuji apple cider!")
