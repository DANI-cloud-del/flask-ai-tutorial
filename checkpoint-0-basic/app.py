# Checkpoint 0: Your First Flask App
# This is the simplest possible Flask application

from flask import Flask, render_template

# Create Flask application instance
# __name__ tells Flask where to find templates and static files
app = Flask(__name__)

# Route decorator - defines URL endpoints
@app.route('/')
def home():
    """
    Home page - this function runs when someone visits /
    Returns the home.html template
    """
    return render_template('home.html')

@app.route('/about')
def about():
    """
    About page - accessible at /about
    Returns the about.html template
    """
    return render_template('about.html')

# Only run if this file is executed directly (not imported)
if __name__ == '__main__':
    # debug=True shows helpful error messages and auto-reloads on code changes
    # NEVER use debug=True in production!
    app.run(debug=True)

# To run this app:
# 1. Make sure your virtual environment is activated
# 2. Run: python app.py
# 3. Open http://127.0.0.1:5000 in your browser
