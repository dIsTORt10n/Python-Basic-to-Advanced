class Recipe:
    """Represents a cooking recipe with its details."""

    def __init__(self, recipe_name, ingredients, cooking_time, cooking_instructions):
        """
        Initializes a new Recipe object with the provided details.

        Parameters:
        recipe_name (str): The name of the recipe.
        ingredients (str): A comma-separated list of ingredients.
        cooking_time (str): The time required to cook the recipe.
        cooking_instructions (str): Step-by-step instructions for cooking.
        """
        self.recipe_name = recipe_name  # Store the name of the recipe
        self.ingredients = ingredients  # Store the ingredients
        self.cooking_time = cooking_time  # Store the cooking time
        self.cooking_instructions = cooking_instructions  # Store the cooking instructions

    def display_info(self):
        """Displays the recipe's information in a formatted manner."""
        print(f"Recipe Name: {self.recipe_name}")  # Print the recipe name
        print(f"Ingredients: {self.ingredients}")  # Print the ingredients
        print(f"Cooking Time: {self.cooking_time}")  # Print the cooking time
        # Print the cooking instructions
        print(f"Cooking Instructions: {self.cooking_instructions}")


def create_recipe():
    """Prompts the user for recipe details and creates a new Recipe object."""
    # Get user input for the recipe details
    recipe_name = input("Enter the recipe name: ")  # Prompt for recipe name
    # Prompt for ingredients
    ingredients = input("Enter the ingredients (comma-separated): ")
    cooking_time = input("Enter the cooking time: ")  # Prompt for cooking time
    # Prompt for cooking instructions
    cooking_instructions = input("Enter the cooking instructions: ")

    print("Recipe created successfully!")  # Confirmation message
    # Return a new Recipe object with the provided details
    return Recipe(recipe_name, ingredients, cooking_time, cooking_instructions)


# Main program execution
print("Welcome to Recipe Collection!")  # Welcome message
recipe1 = create_recipe()  # Create a new recipe by calling the function
print("Displaying recipe ...")  # Indicate that the recipe will be displayed
recipe1.display_info()  # Call the method to display the recipe's information
