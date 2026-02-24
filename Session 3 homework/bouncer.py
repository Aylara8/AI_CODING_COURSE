# age = int(input(" Enter your age: "))
# if age >= 18:
#     print("You can vote.")
# else:
#     print("Not eligible to vote yet.")

# for i in range(5):
#     print(f"Question {i+1}: )")



# # 1. Store your questions and answers in a list of dictionaries
# quiz_data = [
#     {"q": "What is the capital of France?", "a": "Paris"},
#     {"q": "What is 5 + 7?", "a": "12"},
#     {"q": "Which planet is known as the Red Planet?", "a": "Mars"},
#     {"q": "Who wrote 'Romeo and Juliet'?", "a": "Shakespeare"},
#     {"q": "What is the boiling point of water (Celsius)?", "a": "100"}
# ]

# score = 0

# # 2. The Loop: It runs once for every item in our list
# for item in quiz_data:
#     user_answer = input(item["q"] + " ")
    
#     # Check if the answer is correct (ignoring capitalization)
#     if user_answer.strip().lower() == item["a"].lower():
#         print("Correct! ✨")
#         score += 1
#     else:
#         print(f"Wrong! The answer was {item['a']}.")

# print(f"\nGame Over! Your final score is {score}/5")


# def run_quiz(questions):
#     """
#     Takes a list of dictionaries, asks questions, 
#     and returns the total integer score.
#     """
#     total_score = 0
    
#     for item in questions:
#         # Ask the question
#         user_reply = input(f"{item['question']} ")
        
#         # Validate the answer
#         if user_reply.strip().lower() == item['answer'].lower():
#             print("Nice job! +1 point.")
#             total_score += 1
#         else:
#             print(f"Not quite. The correct answer was: {item['answer']}")
            
#     return total_score

# # --- How to use it ---
# my_questions = [
#     {"question": "How many legs does a spider have?", "answer": "8"},
#     {"question": "What is the largest ocean?", "answer": "Pacific"},
#     # ... add more here
# ]

# # Call the function and store the result
# final_result = run_quiz(my_questions)

# print(f"--- Quiz Finished! Final Score: {final_result} ---")

# # 1. This is our "bag" of questions
# questions = ["What is 2+2?", "What color is the sky?", "What do cows drink?"]
# answers = ["4", "blue", "water"]

# score = 0

# # 2. This is the loop! 'i' is like a counter (0, 1, 2)
# for i in range(len(questions)):
#     print(questions[i])
#     user_guess = input("Your answer: ")

#     # 3. Check if the user is right
#     if user_guess.lower() == answers[i].lower():
#         print("Correct!")
#         score = score + 1
#     else:
#         print("Oops! Wrong answer.")

# # 4. Show the final result
# print("All done! Your score is:", score)



# def general():
#     quiz_data= [
#         {"q": "Who is known as the 'King of Pop'?", "a": "Michael Jackson"},
#         {"q": "What is the name of the first Harry Potter book?", "a": "Sorcerer's Stone"},
#         {"q": "Who painted the Mona Lisa?", "a": "Leonardo da Vinci"}
#     ]
# print("General Knowledge Quiz")
# score = 0
# for item in quiz_data:
#         user_answer = input(item["q"] + " ")
#         if user_answer.strip().lower() == item["a"].lower():
#             print("Correct! ✨")
#             score += 1
#         else:
#             print(f"Wrong! The answer was {item['a']}.")
#     print(f"Your final score is {score}/{len(quiz_data)}")

# import os

# # 1. A Helper Function for Colors
# def color_text(text, color):
#     colors = {
#         "green": "\033[92m",
#         "red": "\033[91m",
#         "blue": "\033[94m",
#         "yellow": "\033[93m",
#         "bold": "\033[1m",
#         "end": "\033[0m"
#     }
#     return f"{colors.get(color, '')}{text}{colors['end']}"

# # 2. Function to display the menu
# def show_menu(topics):
#     print(color_text("\n=== MEGA QUIZ MENU ===", "bold"))
#     for topic in topics.keys():
#         print(f"[{color_text(topic, 'blue')}]")

# # 3. Function to handle the actual questioning
# def run_quiz_logic(questions):
#     score = 0
#     for item in questions:
#         user_answer = input(f"\n{item['q']} ")
        
#         if user_answer.strip().lower() == item['a'].lower():
#             print(color_text("  Correct! ✨", "green"))
#             score += 1
#         else:
#             print(color_text(f"  Wrong! The answer was: {item['a']}", "red"))
#     return score

# # 4. The Main Engine
# def main():
#     topics = {
#         "Science": [{"q": "Hardest natural substance?", "a": "Diamond"}],
#         "History": [{"q": "Year WWII ended?", "a": "1945"}],
#         "Movies":  [{"q": "Director of Jurassic Park?", "a": "Steven Spielberg"}]
#     }

#     while True:
#         show_menu(topics)
#         choice = input("\nPick a topic (or type 'exit' to quit): ").capitalize()

#         if choice == "Exit":
#             print(color_text("Thanks for playing! Goodbye.", "yellow"))
#             break

#         if choice in topics:
#             final_score = run_quiz_logic(topics[choice])
#             print(f"\nYour score: {color_text(str(final_score), 'bold')}/{len(topics[choice])}")
#         else:
#             print(color_text("Topic not found. Please try again.", "red"))

# if __name__ == "__main__":
#     main()

# import sys

# # 1. COLOR SETTINGS
# # These are constants to make our code easier to read
# GREEN = "\033[92m"
# RED = "\033[91m"
# BLUE = "\033[94m"
# YELLOW = "\033[93m"
# CYAN = "\033[96m"
# BOLD = "\033[1m"
# RESET = "\033[0m"

# def start_quiz():
#     # 2. NEW TOPICS: Geography and Technology
#     topics = {
#         "Geography": [
#             {"q": "Which is the smallest country in the world?", "a": "Vatican City"},
#             {"q": "What is the longest river in the world?", "a": "Nile"},
#             {"q": "Which country has the most islands?", "a": "Sweden"}
#         ],
#         "Technology": [
#             {"q": "What does 'CPU' stand for?", "a": "Central Processing Unit"},
#             {"q": "Who is known as the father of the computer?", "a": "Charles Babbage"},
#             {"q": "Which company created the iPhone?", "a": "Apple"}
#         ]
#     }

#     while True:
#         # 3. DISPLAY COLORFUL MENU
#         print(f"\n{BOLD}{CYAN}===== CHOOSE YOUR CHALLENGE ====={RESET}")
#         for t in topics.keys():
#             print(f"{BLUE}• {t}{RESET}")
        
#         choice = input(f"\n{YELLOW}Select a topic (or type 'quit'): {RESET}").capitalize()

#         if choice == "Quit":
#             print(f"{BOLD}Thanks for playing! 👋{RESET}")
#             break

#         if choice in topics:
#             score = 0
#             questions = topics[choice]
            
#             print(f"\n{BOLD}--- Starting {choice} Quiz ---{RESET}")

#             # 4. THE CORE LOOP
#             for item in questions:
#                 user_ans = input(f"\n{item['q']} {CYAN}-> {RESET}")
                
#                 if user_ans.strip().lower() == item['a'].lower():
#                     print(f"{GREEN}✔ Correct! Well done.{RESET}")
#                     score += 1
#                 else:
#                     print(f"{RED}✘ Wrong! The answer was: {item['a']}{RESET}")

#             # 5. FINAL SCORE DISPLAY
#             print(f"\n{BOLD}FINAL SCORE: {YELLOW}{score}/{len(questions)}{RESET}")
#         else:
#             print(f"{RED}Error: That topic doesn't exist!{RESET}")

# if __name__ == "__main__":
#     start_quiz()