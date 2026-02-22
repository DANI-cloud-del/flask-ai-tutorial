# Checkpoint 4: Database Integration (Final)

## 🎉 Complete AI Chat Application!

This is the final checkpoint with all features:
- ✅ AI-powered responses (Groq)
- ✅ Conversation history (SQLite)
- ✅ View past chats
- ✅ Beautiful UI (Bootstrap)

## Setup Instructions

### 1. Install All Dependencies

```bash
pip install flask flask-sqlalchemy groq python-dotenv markdown
```

Or use requirements.txt from the project root:
```bash
pip install -r ../requirements.txt
```

### 2. Set Up Environment Variables

```bash
cp .env.example .env
# Edit .env and add your Groq API key
```

### 3. Run the Application

```bash
python app.py
```

The database will be created automatically on first run!

### 4. Try It Out

- Visit: http://127.0.0.1:5000
- Go to Chat and ask questions
- View History to see past conversations

## Database Structure

```sql
Table: chat_history
┌────┬──────────┬──────────┬────────────┬────────────┐
│ id │ question │ response │ model_used │  timestamp  │
├────┼──────────┼──────────┼────────────┼────────────┤
│ 1  │ What...  │ Answer.. │ llama-3.3  │ 2026-02-22 │
└────┴──────────┴──────────┴────────────┴────────────┘
```

## Key Concepts

### Database Model

```python
class ChatHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    model_used = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
```

### Creating Records (CREATE)

```python
new_chat = ChatHistory(
    question="What is Flask?",
    response="Flask is a web framework..."
)
db.session.add(new_chat)
db.session.commit()
```

### Reading Records (READ)

```python
# Get all records
chats = ChatHistory.query.all()

# Get with ordering
chats = ChatHistory.query.order_by(ChatHistory.timestamp.desc()).all()

# Get by ID
chat = ChatHistory.query.get(1)
```

## Viewing the Database

### Option 1: Python Shell

```python
python
>>> from app import app, db, ChatHistory
>>> with app.app_context():
...     chats = ChatHistory.query.all()
...     for chat in chats:
...         print(f"{chat.id}: {chat.question}")
```

### Option 2: DB Browser for SQLite

1. Download from [sqlitebrowser.org](https://sqlitebrowser.org/)
2. Open `chat_history.db`
3. View/edit data visually

## Common Database Operations

### Count total chats
```python
total = ChatHistory.query.count()
```

### Filter by date
```python
from datetime import datetime, timedelta
today = datetime.utcnow().date()
todays_chats = ChatHistory.query.filter(
    ChatHistory.timestamp >= today
).all()
```

### Delete a chat
```python
chat = ChatHistory.query.get(1)
db.session.delete(chat)
db.session.commit()
```

## Next Steps: Deployment!

Your app is complete! Ready to deploy to:
- Render (recommended)
- PythonAnywhere
- Railway
- Fly.io

See the main README for deployment instructions.
