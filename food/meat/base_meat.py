class BaseMeat:
    """Base class for all meats.
    """
    def __init__(self, name, animal):
        """Initialize a BaseMeat instance.

        Args:
            name (str): The name of the meat.
            animal (str): The animal from which the meat is sourced.
        """
        self.name = name
        self.animal = animal

    def describe(self):
        """Return a description of the meat.
        
        Returns:
            str: A description of the meat.
        """
        return f"{self.name} comes from {self.animal}."
