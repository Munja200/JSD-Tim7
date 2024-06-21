import base64
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

def generate_recipe(recipe_model):
    env = Environment(loader=FileSystemLoader('src/templates'), autoescape=select_autoescape(['html', 'xml']))
    template = env.get_template('recipeTemplate.jinja')
    html_output = template.render(model=recipe_model)

    # Save the rendered HTML to a file
    with open('output.html', 'w', encoding='utf-8') as f:
        f.write(html_output)