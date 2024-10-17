import random

# Simple text classification
def classify_text(text):
    categories = {
        'greeting': ['hello', 'hi', 'hey'],
        'farewell': ['goodbye', 'bye', 'see you'],
        'question': ['how', 'what', 'why', 'where']
    }
    for category, keywords in categories.items():
        if any(keyword in text.lower() for keyword in keywords):
            return category
    return 'unknown'

# Simple chatbot responses
def chatbot_response(text):
    responses = {
        'greeting': ['Hello! How can I help you?', 'Hi there! What’s up?', 'Hey! How can I assist?'],
        'farewell': ['Goodbye! Have a great day!', 'Bye! Take care!', 'See you later!'],
        'question': ['I’m not sure. Can you please clarify?', 'That’s an interesting question. Let me think.', 'I don’t know, but I’ll try to help.']
    }
    category = classify_text(text)
    return random.choice(responses.get(category, ['Sorry, I didn’t understand that.']))

# Basic calculator
def calculate(expression):
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"

# Main function
def main():
    print("Welcome to the multi-purpose AI!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye!")
            break
        elif user_input.lower().startswith("calc "):
            expression = user_input[5:]
            result = calculate(expression)
            print(f"Result: {result}")
        else:
            response = chatbot_response(user_input)
            print(f"AI: {response}")

if __name__ == "__main__":
    main()
