from app import app, db
from models import Recipe

with app.app_context():
    # Recipe 1
    recipe1 = Recipe(
        name='Classic Pancakes',
        ingredients='1 1/2 cups all-purpose flour\n3 1/2 teaspoons baking powder\n1 teaspoon salt\n1 tablespoon white sugar\n1 1/4 cups milk\n1 egg\n3 tablespoons butter, melted',
        instructions='In a large bowl, sift together the flour, baking powder, salt, and sugar. Make a well in the center and pour in the milk, egg, and melted butter; mix until smooth.',
        categories='Breakfast, Vegetarian',
        prep_time='10 minutes',
        cook_time='15 minutes',
        total_time='25 minutes',
        yield_='4 servings',
        description='Fluffy and delicious classic pancakes perfect for breakfast.',
        variations='Add blueberries or chocolate chips for extra flavor.',
        main_image='https://example.com/images/classic_pancakes.jpg',
        extra_images='https://example.com/images/classic_pancakes_step1.jpg, https://example.com/images/classic_pancakes_step2.jpg',
        related='French Toast, Waffles'
    )
    db.session.add(recipe1)

    # Recipe 2
    recipe2 = Recipe(
        name='Chicken Stir Fry',
        ingredients='1 pound chicken breast\n2 cups mixed vegetables\n2 tablespoons soy sauce\n1 tablespoon olive oil',
        instructions='Heat oil in a large skillet over medium-high heat. Add chicken and cook until browned. Add vegetables and soy sauce, and stir-fry until vegetables are tender.',
        categories='Dinner, Asian',
        prep_time='15 minutes',
        cook_time='10 minutes',
        total_time='25 minutes',
        yield_='2 servings',
        description='Quick and easy chicken stir fry with fresh vegetables.',
        variations='Try adding tofu or different vegetables for variety.',
        main_image='https://example.com/images/chicken_stir_fry.jpg',
        extra_images='https://example.com/images/chicken_stir_fry_step1.jpg, https://example.com/images/chicken_stir_fry_step2.jpg',
        related='Beef Stir Fry, Vegetable Stir Fry'
    )
    db.session.add(recipe2)

    db.session.commit()
