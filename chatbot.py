import random
from datetime import datetime

def greet():
    greetings = ["Hi there! 👋", "Hello! 😊", "Hey! How can I help you? 🤖"]
    return random.choice(greetings)

def time_based_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning! ☀️"
    elif 12 <= hour < 18:
        return "Good afternoon! 🌤️"
    else:
        return "Good evening! 🌙"

def mood_response():
    moods = [
        "I'm just a bot, but I'm functioning well! ⚙️",
        "Doing great! Hope you're having a productive day. 💻",
        "Feeling electric ⚡ — how about you?"
    ]
    return random.choice(moods)

def farewell():
    farewells = ["Goodbye! 👋", "See you next time! 👋", "Take care! 🤗"]
    return random.choice(farewells)

def unknown():
    responses = [
        "Hmm... I didn’t get that. 🤔",
        "Can you try rephrasing it? 🧐",
        "I'm not sure I understand. 😅"
    ]
    return random.choice(responses)

# 🎮 Mini Game 1: Guess the Number
def guess_the_number():
    number = random.randint(1, 10)
    print("🎲 I'm thinking of a number between 1 and 10. Can you guess it?")
    try:
        guess = int(input("Your guess: "))
        if guess == number:
            print("🎉 Correct! You're lucky!")
        else:
            print(f"❌ Nope! I was thinking of {number}.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# 🎮 Mini Game 2: Rock, Paper, Scissors
def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    bot_choice = random.choice(choices)
    user_choice = input("Your move (rock/paper/scissors): ").lower()

    if user_choice not in choices:
        print("⚠️ Invalid choice. Please try again.")
        return

    print(f"🤖 I chose {bot_choice}!")
    if user_choice == bot_choice:
        print("🤝 It's a tie!")
    elif (user_choice == "rock" and bot_choice == "scissors") or \
         (user_choice == "paper" and bot_choice == "rock") or \
         (user_choice == "scissors" and bot_choice == "paper"):
        print("🎉 You win!")
    else:
        print("😢 I win!")

# 🎮 Mini Game 3: Math Quiz
def math_quiz():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(["+", "-", "*"])

    correct = eval(f"{a} {op} {b}")
    answer = input(f"🧠 What is {a} {op} {b}? ")

    try:
        if int(answer) == correct:
            print("✅ Correct!")
        else:
            print(f"❌ Wrong. The correct answer is {correct}.")
    except ValueError:
        print("⚠️ Please enter a number.")

# 🤖 Chatbot Logic
def chatbot():
    print("🤖 Welcome to CodeAlphaBot — your friendly Python chatbot!")
    print("🗨️ Type something to chat with me. (Type 'exit' to end)\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "exit":
            confirm = input("Bot: Are you sure you want to exit? (yes/no): ").lower()
            if confirm == "yes":
                print("Bot:", farewell())
                break
            else:
                print("Bot: Alright, let's keep chatting! 😄")
        elif user_input in ["hi", "hello", "hey"]:
            print("Bot:", time_based_greeting(), greet())
        elif user_input in ["how are you", "how are you doing"]:
            print("Bot:", mood_response())
        elif user_input in ["bye", "goodbye", "see you"]:
            print("Bot:", farewell())
            break
        elif user_input in ["who are you", "what is your name"]:
            print("Bot: I’m CodeAlphaBot 🤖 — built by a Python intern at CodeAlpha!")
        elif "help" in user_input:
            print("Bot: I can chat, play mini-games, and keep you company. Try typing 'play game' or 'guess number'.")
        elif user_input in ["what can you do", "features"]:
            print("Bot: I can greet, tell the time of day, and even play games like 'guess the number', 'rock paper scissors', and 'math quiz'! 🎮")
        elif user_input == "play game":
            print("Bot: Choose a game — 'guess number', 'rock paper scissors', or 'math quiz'")
        elif user_input == "guess number":
            guess_the_number()
        elif user_input == "rock paper scissors":
            rock_paper_scissors()
        elif user_input == "math quiz":
            math_quiz()
        else:
            print("Bot:", unknown())

# Start the chatbot
chatbot()
