from queries import get_recipe



def generate_normal_text():
    recipe = get_recipe()

    text = f"""Название рецепта: {recipe[0][1]}
Ингредиенты:
------------\n"""
    c = 0
    for ing in recipe[1]:
        c += 1
        text += f"""\t\t\t{c}.{ing[0]}\n"""

    text += f"""Инструкция приготовления:
-------------------------\n"""
    n = 0
    for ins in recipe[2]:
        n += 1
        text += f"""\t\t\t{n}. {ins[0]}\n"""


    photo = recipe[0][9]
    
    return text, photo





