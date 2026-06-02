import random
from datetime import datetime

greetings = [
    "Hello!",
    "Hi there!",
    "Greetings!",
    "Hey! Nice to see you.",
    "Welcome back!"
]

farewells = [
    "Goodbye!",
    "See you soon!",
    "Have a great day!",
    "Take care!",
    "Thanks for using Decode AI!"
]

quotes = [
    "Success is the sum of small efforts repeated day in and day out.",
    "The expert in anything was once a beginner.",
    "Dream big. Start small. Act now.",
    "Consistency beats motivation.",
    "Your future is created by what you do today.",
    "Small progress is still progress.",
    "Believe in yourself and all that you are."
]

programming_knowledge = {
    "python": "Python is a beginner-friendly language widely used in AI, Data Science, Web Development, and Automation.",
    "java": "Java is an object-oriented language used in enterprise applications, Android development, and backend systems.",
    "c++": "C++ is powerful for competitive programming, game development, and system programming.",
    "javascript": "JavaScript powers interactive websites and is essential for frontend and full-stack development.",
    "dsa": "Data Structures and Algorithms are crucial for coding interviews and problem-solving.",
    "web development": "Web Development includes HTML, CSS, JavaScript, backend technologies, databases, and deployment.",
    "ai": "Artificial Intelligence enables machines to simulate human intelligence and decision-making."
}

college_guidance = {
    "internship": "Build projects, practice DSA, maintain GitHub, improve LinkedIn, and apply consistently.",
    "resume": "Keep your resume one page, include projects, skills, achievements, and relevant experience.",
    "placement": "Focus on DSA, projects, communication skills, aptitude, and mock interviews.",
    "cgpa": "Maintain a good CGPA while developing practical skills and building projects.",
    "hackathon": "Participate in hackathons to learn teamwork, build projects, and improve problem-solving.",
    "project": "Projects demonstrate practical skills and help strengthen your resume."
}

basic_responses = {
    "how are you": "I'm doing great! How can I help you today?",
    "who are you": "I am Decode AI, your personal student assistant.",
    "what is your name": "My name is Decode AI.",
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    "help": "Type commands like: time, date, quote, python, java, internship, about, exit.",
    "about": "Decode AI v1.0 | A Rule-Based AI Assistant built using Python for DecodeLabs Project 1."
}

print("=" * 60)
print("                    DECODE AI")
print("=" * 60)
print("      Your Personal Student Assistant")
print("=" * 60)

user_name = input("\nDecode AI: What's your name? ").strip().title()

if not user_name:
    user_name = "User"

print(f"\nDecode AI: Welcome, {user_name}! 🚀")
print("Type 'help' to see available commands.\n")

message_count = 0
session_start = datetime.now()

while True:

    user_input = input(f"\n{user_name}: ").strip().lower()

    message_count += 1

    if user_input in ["exit", "quit", "bye", "goodbye", "stop"]:

        print("\nDecode AI:", random.choice(farewells))

        print("\n" + "=" * 60)
        print("SESSION SUMMARY")
        print("=" * 60)
        print(f"User Name : {user_name}")
        print(f"Messages  : {message_count}")
        print(f"Started   : {session_start.strftime('%I:%M %p')}")
        print(f"Ended     : {datetime.now().strftime('%I:%M %p')}")
        print("=" * 60)

        break

    elif user_input in [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]:

        print("Decode AI:", random.choice(greetings))

    elif "what is my name" in user_input:
        print(f"Decode AI: Your name is {user_name}.")

    elif user_input in ["time", "current time"]:

        current_time = datetime.now().strftime("%I:%M:%S %p")
        print(f"Decode AI: Current Time is {current_time}")

    elif user_input in ["date", "today", "current date"]:

        current_date = datetime.now().strftime("%d %B %Y")
        print(f"Decode AI: Today's Date is {current_date}")

    elif user_input in [
        "quote",
        "motivation",
        "motivate me",
        "inspire me"
    ]:

        print("Decode AI:", random.choice(quotes))

    elif user_input in basic_responses:

        print("Decode AI:", basic_responses[user_input])

    elif any(keyword in user_input for keyword in programming_knowledge):

        for keyword in programming_knowledge:
            if keyword in user_input:
                print("Decode AI:", programming_knowledge[keyword])
                break

    elif any(keyword in user_input for keyword in college_guidance):

        for keyword in college_guidance:
            if keyword in user_input:
                print("Decode AI:", college_guidance[keyword])
                break

    elif user_input == "menu":

        print("\n========== AVAILABLE COMMANDS ==========")
        print("Greetings       -> hello, hi, hey")
        print("Date & Time     -> date, time")
        print("Motivation      -> quote, motivate me")
        print("Programming     -> python, java, c++, javascript, dsa")
        print("College Help    -> internship, resume, placement")
        print("Memory          -> what is my name")
        print("About           -> about")
        print("Exit            -> exit")
        print("========================================")

    else:

        print(
            "Decode AI: Sorry, I don't understand that. Type 'help' or 'menu' to see available commands."
        )