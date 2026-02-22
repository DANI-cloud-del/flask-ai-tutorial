# Checkpoint 4: Flask with Database Integration (Final)
# Complete AI chat app with conversation history stored in SQLite

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from groq import Groq
import os
from dotenv import load_dotenv
import markdown

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat_history.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Initialize Groq client
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

# Database Model
class ChatHistory(db.Model):
    """Stores chat conversations"""
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    model_used = db.Column(db.String(100), default='llama-3.3-70b-versatile')
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Chat {self.id}: {self.question[:30]}...>'

# Create database tables
with app.app_context():
    db.create_all()
    print("Database initialized!")

@app.route('/')
def home():
    """Home page"""
    return render_template('home.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    """Chat page with AI and database storage"""
    if request.method == 'POST':
        user_question = request.form.get('question')
        
        try:
            # Call Groq API
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
                model="llama-3.3-70b-versatile",
                temperature=0.7,
                max_tokens=1024
            )
            
            ai_response = chat_completion.choices[0].message.content
            
            # Save to database
            new_chat = ChatHistory(
                question=user_question,
                response=ai_response,
                model_used="llama-3.3-70b-versatile"
            )
            db.session.add(new_chat)
            db.session.commit()
            
            # Convert to HTML for display
            ai_response_html = markdown.markdown(ai_response)
            
        except Exception as e:
            ai_response_html = f"<p class='text-danger'>Error: {str(e)}</p>"
        
        return render_template('chat.html',
                             question=user_question,
                             response=ai_response_html)
    
    return render_template('chat.html')

@app.route('/history')
def history():
    """Display all past conversations"""
    # Get all chats, newest first
    chats = ChatHistory.query.order_by(ChatHistory.timestamp.desc()).all()
    return render_template('history.html', chats=chats)

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

# Key concepts in this checkpoint:
# 1. SQLAlchemy database models
# 2. CRUD operations (Create, Read)
# 3. Database queries and ordering
# 4. Storing AI conversations for history
# 5. Displaying database records in templates
