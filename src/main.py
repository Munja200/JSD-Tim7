from generator import generator
from metamodel import recipe
import logging


def main():
    try:
        generator.generate_recipe(recipe.init_recipe_metamodel())
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    main()