# Checkpoint 3: Flask with AI Integration (Groq API)
# This checkpoint adds real AI responses using Groq API

from flask import Flask, render_template, request
from groq import Groq
import os
from dotenv import load_dotenv
import markdown

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')

# Initialize Groq client
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

@app.route('/')
def home():
    """Home page"""
    return render_template('home.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    """
    Chat page with real AI integration
    """
    if request.method == 'POST':
        user_question = request.form.get('question')
        
        try:
            # Call Groq API for AI response
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful AI assistant for students. Provide clear, concise answers with examples when helpful."
                    },
                    {
                        "role": "user",
                        "content": user_question
                    }
                ],
                model="llama-3.3-70b-versatile",  # Fast and powerful model
                temperature=0.7,  # Controls randomness (0 = deterministic, 2 = very creative)
                max_tokens=1024  # Maximum length of response
            )
            
            # Extract AI response
            ai_response = chat_completion.choices[0].message.content
            
            # Convert markdown to HTML for better formatting
            ai_response_html = markdown.markdown(ai_response)
            
        except Exception as e:
            # Handle errors gracefully
            ai_response_html = f"<p class='text-danger'>Sorry, I encountered an error: {str(e)}</p>"
            ai_response_html += "<p>Make sure you've set up your .env file with GROQ_API_KEY</p>"
        
        return render_template('chat.html',
                             question=user_question,
                             response=ai_response_html)
    
    return render_template('chat.html')

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

# Key concepts in this checkpoint:
# 1. Environment variables with python-dotenv
# 2. Groq API client initialization
# 3. API request structure (system message + user message)
# 4. Error handling with try/except
# 5. Markdown rendering for formatted responses
