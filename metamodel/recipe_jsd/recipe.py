import os

from model import Recept
from textx import metamodel_from_file, language
from textx.export import model_export

def recipe_processor(info):
    return Recept(vrednost=1, alergeni=[], ime=info.name, opis=info.opis, url=info.url, vrsta=info.vrsta, vreme=info.vreme, sastojci=info.sastojci, upustvo=info.uputstvo, nutVrednost=info.nutVrednost, saveti=info.saveti)


def init_cv_metamodel():
    cv_grammar_path = 'recipe.tx'
    cv_metamodel = metamodel_from_file(cv_grammar_path)
    print('radi ovo sad')
    cv_metamodel.register_obj_processors({'Recept': recipe_processor})

    robot_model = cv_metamodel.model_from_file('../../example/recipe_example.rcp')
    model_export(robot_model,'program.dot')
    print(robot_model.recepti[0].vrednost, "  Ovo su alergeni  ", robot_model.recepti[0].alergeni)
    for nam in  robot_model.namirnice:
        print(nam.imeNamirnice)
    return cv_metamodel


@language('recipe', '*.rcp')
def cv_parser():
    return init_cv_metamodel()

def main():
    cv_file_path = 'examples/example1.cv'

    init_cv_metamodel()

if __name__ == '__main__':
    main()
