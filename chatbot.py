import random

def simple_chatbot(user_input, user_name=""):
    user_input = user_input.lower()  # Normalize input to lowercase

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"

    elif "how are you" in user_input:
        return random.choice([
            "I'm just a program, but thanks for asking!",
            "Doing well, how about you?",
            "I'm here and ready to assist!"
        ])

    elif "your name" in user_input:
        return "I'm a simple chatbot created to help you. You can call me Chatbot!"

    elif "my name is" in user_input:
        user_name = user_input.split("my name is ")[1].strip()
        return f"Nice to meet you, {user_name}!"

    elif user_name and "what's my name" in user_input:
        return f"Your name is {user_name}."

    elif "help" in user_input:
        return "Sure! What do you need help with?"

    elif "thank you" in user_input:
        return "You're welcome! If you have any other questions, feel free to ask."

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"

    else:
        return "I'm sorry, I didn't understand that. Can you rephrase?"

# Example interaction
user_name = ""
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = simple_chatbot(user_input, user_name)
    if "Nice to meet you" in response:
        user_name = response.split(", ")[-1].strip("!")  # Update user_name
    print(f"Chatbot: {response}")
