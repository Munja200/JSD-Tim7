from generator import generator
from metamodel import recipe
import logging
import sys

import os


def main():
    try:
        print(sys.argv[1:])
        args = sys.argv[1:]
        current_directory = os.getcwd()
        print(current_directory)
        if len(args) == 0:
            generator.generate_recipe(recipe.init_recipe_metamodel())
        elif len(args) == 1:
            generator.generate_recipe(recipe.init_recipe_metamodel(args[0]))
        elif len(args) == 2:
            generator.generate_recipe(recipe.init_recipe_metamodel(args[0]), args[1])
        else:
            logging.exception("Losi argumenti")
            
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    main()