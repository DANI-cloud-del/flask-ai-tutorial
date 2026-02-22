# Checkpoint 2: Flask with Forms and User Input
# This checkpoint adds form handling and POST requests

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    """Home page"""
    return render_template('home.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    """
    Chat page that handles both GET and POST requests
    GET: Display empty form
    POST: Process form submission and display result
    """
    if request.method == 'POST':
        # Get the user's question from the form
        user_question = request.form.get('question')
        
        # For now, just echo it back (we'll add real AI in Checkpoint 3)
        ai_response = f"You asked: {user_question}\n\nThis is a placeholder response. In the next checkpoint, we'll integrate real AI!"
        
        # Render template with both question and response
        return render_template('chat.html', 
                             question=user_question,
                             response=ai_response)
    
    # If GET request, just show the empty form
    return render_template('chat.html')

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

# Key concepts in this checkpoint:
# 1. methods=['GET', 'POST'] - Handle multiple HTTP methods
# 2. request.method - Check which method was used
# 3. request.form.get() - Get form data from POST request
# 4. Passing variables to templates
