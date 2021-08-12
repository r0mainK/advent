from collections import Counter
from pathlib import Path


allergen_to_ingredient = {}
ingredient_counter = Counter()

with (Path(__file__).parent / "data" / "21.txt").open() as fin:
    for ingredients in map(str.strip, fin):
        allergens = []
        if "contains" in ingredients:
            ingredients, allergens = ingredients.split("(contains")
            allergens = allergens.replace(")", "").replace(",", "").strip().split()
        ingredients = set(ingredients.strip().split())
        for allergen in allergens:
            previous_ingredients = allergen_to_ingredient.get(allergen, ingredients)
            allergen_to_ingredient[allergen] = previous_ingredients.intersection(ingredients)
        ingredient_counter.update(ingredients)

dangerous_ingredients = {
    ingredient for ingredients in allergen_to_ingredient.values() for ingredient in ingredients
}
total_count = 0
for ingredient, count in ingredient_counter.items():
    if ingredient not in dangerous_ingredients:
        total_count += count

print(f"times allergen-free ingredients appear: {total_count}")

allergens = {}
seen_ingredients = set()
while len(allergens) < len(allergen_to_ingredient):
    for allergen, ingredients in allergen_to_ingredient.items():
        possible_ingredients = list(ingredients - seen_ingredients)
        if len(possible_ingredients) == 1:
            allergens[allergen] = possible_ingredients[0]
            seen_ingredients.add(possible_ingredients[0])

print(
    "canonical dangerous ingredients list: "
    f"{','.join(allergens[allergen] for allergen in sorted(allergens))}"
)
