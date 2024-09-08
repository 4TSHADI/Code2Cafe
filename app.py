from flask import Flask, render_template, request, redirect, url_for
from models import db, Recipe
from sqlalchemy import or_
from flask_migrate import Migrate  # Import Flask-Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

def get_all_categories():
    categories = set()
    recipes = Recipe.query.all()
    for recipe in recipes:
        for category in recipe.categories.split(','):
            categories.add(category.strip())
    return sorted(categories)

@app.route('/')
def index():
    recipes = Recipe.query.all()
    categories = get_all_categories()
    return render_template('index.html', recipes=recipes, categories=categories)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    if query:
        recipes = Recipe.query.filter(
            or_(
                Recipe.name.ilike(f'%{query}%'),
                Recipe.ingredients.ilike(f'%{query}%')
            )
        ).all()
    else:
        recipes = []
    categories = get_all_categories()
    return render_template('search_results.html', recipes=recipes, query=query, categories=categories)

@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    categories = get_all_categories()
    return render_template('recipe_detail.html', recipe=recipe, categories=categories)

@app.route('/category/<category_name>')
def category(category_name):
    recipes = Recipe.query.filter(Recipe.categories.ilike(f'%{category_name}%')).all()
    categories = get_all_categories()
    return render_template('index.html', recipes=recipes, categories=categories, selected_category=category_name)

if __name__ == '__main__':
    app.run(debug=True)
