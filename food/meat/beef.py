from food.meat.base_meat import BaseMeat

class Beef(BaseMeat):
    """Beef meat class"""

    def __init__(self, name="Beef", animal="cow"):
        """Initialize a Beef instance.
        
        Args:
            name (str): The name of the meat. Default is "Beef".
            animal (str): The animal from which the meat is sourced. Default is "cow".
        """
        super().__init__(name, animal)

    def cook_steak(self, size="medium"):
        """Cook a steak of a given size.

        Args:
            size (str): The size of the steak. Default is "medium".
        """
        print(f"Cooking a {size} steak!")

class Wagyu(Beef):
    """Wagyu beef class"""

    def __init__(self, name="Wagyu Beef", animal="cow"):
        """Initialize a Wagyu Beef instance.

        Args:
            name (str): The name of the meat. Default is "Wagyu Beef".
            animal (str): The animal from which the meat is sourced. Default is "cow".
        """
        super().__init__(name, animal)
    
    def cook_sukiyaki(self, size="large"):
        """Cook sukiyaki of a given size.

        Args:
            size (str): The size of the sukiyaki. Default is "large".
        """
        print(f"Cooking {size} sukiyaki with premium Wagyu beef!")
