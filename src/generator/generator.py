import base64
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from utils import module_path

def generate_recipe(recipe_model):
    env = Environment(loader=FileSystemLoader(module_path('templates')), autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('recipeTemplate.jinja')
    html_output = template.render(model=recipe_model, slika1=module_path('icons\stopwatch.png'), slika2=module_path('icons\calories-calculator.png'))
    print(module_path('icons\stopwatch.png'))
    current_directory = os.getcwd()
    output_file_name = 'output.html'
    path = os.path.join(current_directory,output_file_name)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html_output)