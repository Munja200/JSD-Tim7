from setuptools import setup, find_packages

setup(
    name='JSD_project',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'Arpeggio == 2.0.2',
        'click == 8.1.7',
        'colorama == 0.4.6',
        'textX == 4.0.1',
        'twine==5.0.0',
        'setuptools==69.1.0',
        'wheel==0.43.0'
    ],
    package_data={
        "": ["metamodel/recipe_jsd/*.tx", "templates/*.jinja"]
    },
    entry_points={
        'textx_languages': [
            'recipe_lang = metamodel.recipe_jsd.recipe:rcp_parser',
        ],
        'textx_generators': [
            'recipe_gen = generator.recipe_generator.generator:rcp_generator',
        ]
    },
)