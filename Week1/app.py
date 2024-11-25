def chat():
    print("Bot: Hello! I'm a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Bot: Goodbye!")
            break
        print(f"Bot: You said: {user_input}")

if __name__ == "__main__":
    chat()