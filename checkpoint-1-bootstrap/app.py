# Checkpoint 1: Flask with Bootstrap
# This checkpoint adds Bootstrap styling and template inheritance

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Home page with Bootstrap styling"""
    return render_template('home.html')

@app.route('/about')
def about():
    """About page with Bootstrap styling"""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

# Key improvements in this checkpoint:
# 1. base.html template with Bootstrap CDN
# 2. Template inheritance using {% extends %}
# 3. Bootstrap components (navbar, cards, buttons)
# 4. Responsive design out of the box
