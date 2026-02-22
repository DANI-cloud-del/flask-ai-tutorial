# Checkpoint 3: AI Integration with Groq

## What's New

- Real AI responses using Groq API
- Environment variable management
- Markdown rendering for formatted responses
- Error handling for API calls

## Setup Instructions

### 1. Install Dependencies

```bash
pip install flask groq python-dotenv markdown
```

### 2. Get Groq API Key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key (you can't see it again!)

### 3. Set Up Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your keys
```

**Your .env file should look like:**
```
FLASK_SECRET_KEY=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
GROQ_API_KEY=gsk_your_actual_groq_api_key_here
```

### 4. Run the Application

```bash
python app.py
```

### 5. Test It Out

Go to http://127.0.0.1:5000/chat and try asking:
- "Explain machine learning in simple terms"
- "What is Flask used for?"
- "Write a Python function to calculate factorial"

## How It Works

### Groq API Call Structure

```python
chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": user_question}
    ],
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=1024
)
```

**Parameters explained:**
- **system message**: Sets AI's behavior/personality
- **user message**: The actual question
- **model**: Which AI model to use (llama-3.3-70b is fast and powerful)
- **temperature**: Randomness (0 = predictable, 2 = creative)
- **max_tokens**: Maximum response length

### Environment Variables

**Why use .env files?**
- ✅ Keep secrets out of code
- ✅ Different keys for dev/production
- ✅ Easy to update without code changes
- ✅ Never accidentally commit API keys

## Common Issues

### Error: "No module named 'groq'"

**Solution:**
```bash
pip install groq python-dotenv markdown
```

### Error: "GROQ_API_KEY not found"

**Solution:**
1. Make sure .env file exists
2. Check that .env contains `GROQ_API_KEY=your_key`
3. Restart Flask after creating .env

### Error: "Invalid API key"

**Solution:**
1. Verify your API key is correct
2. Make sure you copied the entire key
3. Generate a new key if needed

## Next Steps

In Checkpoint 4, we'll add:
- Database to store chat history
- View past conversations
- Search through history
