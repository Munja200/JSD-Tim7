import os

from model import Recept
from textx import metamodel_from_file, language
from textx.export import model_export

def recipe_processor(info):
    return Recept(vrednost=0, alergeni=[], ime=info.name, opis=info.opis, url=info.url, vrsta=info.vrsta, vreme=info.vreme, sastojci=info.sastojci, upustvo=info.uputstvo, nutVrednost=info.nutVrednost, saveti=info.saveti)

def knjiga_recepata(model):
    for recept in model.recepti:
        recept.vrednost =  kalorijska_vrednost_recepta(model.namirnice, recept.sastojci)
        recept.alergeni = svi_alergeni_recepta(model.namirnice, recept.sastojci)
    return model

def init_cv_metamodel():
    cv_grammar_path = 'recipe.tx'
    cv_metamodel = metamodel_from_file(cv_grammar_path)
    cv_metamodel.register_obj_processors({'KnjigaRecepata': knjiga_recepata,'Recept': recipe_processor})

    robot_model = cv_metamodel.model_from_file('../../example/recipe_example.rcp')
    model_export(robot_model,'program.dot')

    return cv_metamodel


@language('recipe', '*.rcp')
def cv_parser():
    return init_cv_metamodel()

def kalorijska_vrednost_recepta(namirnice, sastojci):
    vrednost = 0
    for sastojak in sastojci:
        namirnica=dobavi_namjernicu_po_imenu_sastojka(sastojak.imeSastojka, namirnice)
        if sastojak.jedinicaMase == 'KG' or sastojak.jedinicaMase == 'kg':
            vrednost = vrednost + sastojak.kolicina * 1000 * namirnica.nutVrednost.vrednost / namirnica.nutVrednost.kolicina
        else:
            vrednost = vrednost + sastojak.kolicina * namirnica.nutVrednost.vrednost / namirnica.nutVrednost.kolicina
    return vrednost


def dobavi_namjernicu_po_imenu_sastojka(ime_sastojka, namjernice):
    for namjernica in namjernice:
        if namjernica.imeNamirnice.lower() == ime_sastojka.lower():
            if namjernica.nutVrednost.jedinicaMase == 'KG' or namjernica.nutVrednost.jedinicaMase == 'kg':
                namjernica.nutVrednost.kolicina = namjernica.nutVrednost.kolicina * 1000
                namjernica.nutVrednost.jedinicaMase = 'g'
            return  namjernica
    return

def svi_alergeni_recepta(namirnice, sastojci):
    alergeni=[]
    for sastojak in sastojci:
        namirnica = dobavi_namjernicu_po_imenu_sastojka(sastojak.imeSastojka, namirnice)
        if  len(namirnica.alergeni) > 0:
            alergeni.extend(namirnica.alergeni)
    return alergeni

def main():
    cv_file_path = 'examples/example1.cv'

    init_cv_metamodel()

if __name__ == '__main__':
    main()

