from food.meat.base_meat import BaseMeat

class Pork(BaseMeat):
    """Pork meat class
    """
    def __init__(self, name="Pork", animal="pig"):
        """Initialize a Pork instance.

        Args:
            name (str): The name of the meat. Default is "Pork".
            animal (str): The animal from which the meat is sourced. Default is "pig".
        """
        super().__init__(name, animal)

    def cook_bacon(self, size="medium"):
        """Cook bacon of a given size.

        Args:
            size (str): The size of the bacon. Default is "medium".
        """
        print(f"Cooking {size} crispy bacon!")
