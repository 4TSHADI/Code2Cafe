from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    categories = db.Column(db.String(100), nullable=False)
    
    # Optional columns
    prep_time = db.Column(db.String(50))  # e.g., "15 minutes"
    cook_time = db.Column(db.String(50))  # e.g., "30 minutes"
    total_time = db.Column(db.String(50))  # e.g., "45 minutes"
    yield_ = db.Column(db.String(50))  # Number of servings or portions
    description = db.Column(db.Text)  # Description of the recipe
    variations = db.Column(db.Text)  # Variations or modifications
    main_image = db.Column(db.String(255))  # URL or path to the main image
    extra_images = db.Column(db.Text)  # URLs or paths to extra images (comma-separated or JSON)
    related = db.Column(db.Text)  # Related recipes or pairings (comma-separated or JSON)
