# Checkpoint 0: Basic Flask App

## What This Checkpoint Covers

- Creating a minimal Flask application
- Defining routes with `@app.route()`
- Rendering HTML templates
- Basic navigation between pages

## Project Structure

```
checkpoint-0-basic/
├── app.py              # Main Flask application
└── templates/          # HTML templates folder
    ├── home.html       # Home page
    └── about.html      # About page
```

## Setup Instructions

### 1. Create Virtual Environment

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

### 2. Install Flask

```bash
pip install flask
```

### 3. Run the Application

```bash
python app.py
```

### 4. Open in Browser

Go to: http://127.0.0.1:5000

## What You'll See

- A simple home page with a welcome message
- Navigation links to Home and About pages
- An about page with information

## Key Concepts

### Routes

```python
@app.route('/')
def home():
    return render_template('home.html')
```

- `@app.route('/')` - Decorator that maps URL `/` to the function
- `home()` - Function that handles requests to `/`
- `render_template()` - Renders an HTML file from the templates folder

### Templates Folder

Flask automatically looks for templates in a folder named `templates/`:
- Must be spelled exactly as `templates` (not `template`)
- Must be in the same directory as `app.py`

## Common Issues

### Error: "TemplateNotFound: home.html"

**Solution:**
1. Check that folder is named `templates` (not `template`)
2. Verify `home.html` is directly inside `templates/`
3. Check spelling and capitalization

### Error: "Address already in use"

**Solution:**
1. Flask is already running in another terminal
2. Close the other terminal or press Ctrl+C
3. Or change port: `app.run(debug=True, port=5001)`

## Next Steps

Once this works, move to **Checkpoint 1** to add:
- Bootstrap styling
- Template inheritance
- Professional-looking UI
