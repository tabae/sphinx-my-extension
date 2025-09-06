from food.fruit.base_fruit import BaseFruit

class Banana(BaseFruit):
    """A class representing a banana fruit.
    """
    def __init__(self, name="Banana", color="yellow"):
        """Initialize a Banana instance.

        Args:
            name (str): The name of the banana variety. Default is "Banana".
            color (str): The color of the banana. Default is "yellow".
        """
        super().__init__(name, color)

    def make_smoothie(self, size="medium"):
        """Make a banana smoothie of a given size.

        Args:
            size (str): The size of the smoothie. Default is "medium".
        """
        print(f"Making {size} banana smoothie!")
