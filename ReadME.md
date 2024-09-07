# Recipe Website

A simple web application for browsing and searching recipes. Built with Flask for the backend and server-side rendering, minimizing JavaScript use.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Setup](#setup)
- [Usage](#usage)
- [Database Setup](#database-setup)
- [Contributing](#contributing)
- [License](#license)

## Features
- Browse recipes and search by name or ingredient.
- Filter recipes by categories.
- View detailed recipe information.
- Recipes can belong to multiple categories.

## Technologies
- **Backend**: Flask (Python)
- **Database**: SQLite (via SQLAlchemy)
- **Frontend**: HTML, CSS

## Setup

### Prerequisites
- Python 3.6+
- pip (Python package installer)

### Install Dependencies
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd recipe-website
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application
1. Start the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://localhost:5000` to view the application.

## Database Setup

1. **Initialize the Database**:
   The database (`recipes.db`) will be created automatically when you run the Flask application for the first time.

2. **Add Sample Data**:
   To add sample recipes to the database, run the following code in the Python shell or use the provided script:
   ```python
   from app import app, db
   from models import Recipe

   with app.app_context():
       # Recipe 1
       recipe1 = Recipe(
           name='Classic Pancakes',
           ingredients='1 1/2 cups all-purpose flour\n3 1/2 teaspoons baking powder\n1 teaspoon salt\n1 tablespoon white sugar\n1 1/4 cups milk\n1 egg\n3 tablespoons butter, melted',
           instructions='In a large bowl, sift together the flour, baking powder, salt and sugar...\n',
           categories='Breakfast, Vegetarian'
       )
       db.session.add(recipe1)

       # Recipe 2
       recipe2 = Recipe(
           name='Chicken Stir Fry',
           ingredients='1 pound chicken breast\n2 cups mixed vegetables\n2 tablespoons soy sauce\n1 tablespoon olive oil',
           instructions='Heat oil in a large skillet over medium-high heat...\n',
           categories='Dinner, Asian'
       )
       db.session.add(recipe2)

       db.session.commit()
