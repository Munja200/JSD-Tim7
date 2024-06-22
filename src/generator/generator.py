import base64
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from utils import module_path
from textx import GeneratorDesc

def generate_recipe(recipe_model):
    env = Environment(loader=FileSystemLoader(module_path('templates')), autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('recipeTemplate.jinja')
    html_output = template.render(model=recipe_model)
    current_directory = os.getcwd()
    output_file_name = 'output.html'
    path = os.path.join(current_directory,output_file_name)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html_output)

generate_recipe_descriptor = GeneratorDesc(language='recipe', target='html', description='dsl language for creating html pages for recipes', generator=generate_recipe)
    