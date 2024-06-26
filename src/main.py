from generator import generator
from metamodel import recipe
import logging
import sys


def main():
    try:
        args = sys.argv[1:]
        if len(args) == 0:
            generator.generate_recipe(recipe.init_recipe_metamodel())
        elif len(args) == 1:
            generator.generate_recipe(recipe.init_recipe_metamodel(args[0]))
        else:
            logging.exception("Losi argumenti")
            
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    main()