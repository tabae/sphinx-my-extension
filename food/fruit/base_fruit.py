class BaseFruit:
    """A base class for fruits.

    Args:
        name (str): The name of the fruit.
        color (str): The color of the fruit.
    """
    def __init__(self, name, color):
        """Initialize a BaseFruit instance.
        Args:
            name (str): The name of the fruit.
            color (str): The color of the fruit.
        """
        self.name = name
        self.color = color

    def describe(self):
        """Return a description of the fruit.

        Returns:
            str: A description of the fruit.
        """
        return f"{self.name} is {self.color}."
