import os
from textx import language, metamodel_from_file

__version__ = "0.1.0.dev"


@language('recipe', '*.rcp')
def recipe_language():
    "recipe language"
    current_dir = os.path.dirname(__file__)
    mm = metamodel_from_file(os.path.join(current_dir, 'recipe.tx'))

    # Here if necessary register object processors or scope providers
    # http://textx.github.io/textX/stable/metamodel/#object-processors
    # http://textx.github.io/textX/stable/scoping/

    return mm


def init_cv_metamodel():
    cv_grammar_path = 'src/dsl/cv.tx'
    cv_metamodel = metamodel_from_file(cv_grammar_path)


    return cv_metamodel
