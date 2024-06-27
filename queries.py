import psycopg2
import random


def get_recipe():
    no_rec = random.randint(1, 50)

    with psycopg2.connect(
            database="group_12_30",
            host="localhost",
            user="postgres",
            port=5432,
            password=123456
    ) as database:
        cursor = database.cursor()

        cursor.execute("""
        SELECT * FROM meal
        WHERE id = (%s)
        """, (no_rec,))

        meal = cursor.fetchone()

        cursor.execute("""
        SELECT ing_name FROM ingredients
        WHERE meal_id = (%s)
        """, (no_rec,))

        ingredients = cursor.fetchall()

        cursor.execute("""
               SELECT ins_name FROM instructions
               WHERE meal_id = (%s)
               """, (no_rec,))

        instructions = cursor.fetchall()

    return meal, ingredients, instructions
