import sys

def KBC_p():
    # Initialize variables
    eM = 0    # Total earnings
    wrong_ans = 0   # Number of wrong answers

    # Loop through each question
    for question in questions:   
        # Print the question and options
        print(question["question"])
        print(question['options'])  

        # Get user input for answer
        user_input = input("Choose an option: ").upper()

        # Check if the answer is correct
        if user_input == question['answer']:
            print("Great! Correct answer.")

            # Update total earnings if the answer is correct
            eM += 50
            print("Your total earning is: $" + str(eM))
        else:
            print("Oops! Wrong answer.") 

            # Deduct points for wrong answer
            eM -= 60
            print("Your total earning is: $" + str(eM))

            # Increase wrong_ans count
            wrong_ans += 1

            # Check if the player gave three wrong answers
            if wrong_ans == 3:
                print("You gave 3 wrong answers. Better luck next time.")
                sys.exit()

# Welcome message and initial choices
print("         WELCOME TO\n    'KAUN BNEGA CROREPATI'")
print("Select option 'A' to take $50 without playing or select option 'B' to play the game.")
user_input = input("A. $50         B. Play\n").upper()

# Handle user choices
if user_input == 'A':
    print("Congratulations! You earned $50.")
    print('Thanks for participating in KBC!!!')
    sys.exit(0)
elif user_input == 'B': 
    print("Let's start the game with zero money. \n If you give wrong answer more than 2 times your game will automatically end")
else:
    print("Invalid choice.")    
    sys.exit()

# Define the questions list
questions = [
    {
            "question": "1. What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Berlin", "D. Rome"],
            "answer": "A"
        },
        {
            "question": "2.What is the largest planet in our solar system?",
            "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
            "answer": "B"
        },
        {
            "question": "3.Who wrote 'Romeo and Juliet'?",
            "options": ["A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. Mark Twain"],
            "answer": "A"
        },
        {
            "question": "4.Which country is famous for the Great Wall of China?",
            "options": ["A. Japan", "B. China", "C. India", "D. Russia"],
            "answer": "B"
        },
        {
            "question": "5.What is the chemical symbol for gold?",
            "options": ["A. Au", "B. Ag", "C. Fe", "D. Cu"],
            "answer": "A"
        },
        {
            "question": "6.What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Berlin", "D. Rome"],
            "answer": "A"
        },
        {
            "question": "7.What is the largest planet in our solar system?",
            "options": ["A. Earth", "B. Saturn", "C. Jupiter", "D. Mars"],
            "answer": "C"
        },
        {
            "question": "8.Who wrote 'Romeo and Juliet'?",
            "options": ["A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. Mark Twain"],
            "answer": "A"
        },
        {
            "question": "9.What is the symbol for water?",
            "options": ["A. O", "B. W", "C. H", "D. Au"],
            "answer": "C"
        },
        {
            "question": "10.What is the capital of Japan?",
            "options": ["A. Beijing", "B. Tokyo", "C. Seoul", "D. Osaka"],
            "answer": "B"
        },   
        {
            "question": "11.What is the national flower of Pakistan?",
            "options": ["A. Rose", "B. Jasmine", "C. Lotus", "D. Sunflower"],
            "answer": "B"
        },
        {
            "question": "12.Who was the first Prime Minister of India?",
            "options": ["A. Jawaharlal Nehru", "B. Indira Gandhi", "C. Mahatma Gandhi", "D. Narendra Modi"],
            "answer": "A"
        },
        {
            "question": "13.Who holds the record for the highest individual score in One Day Internationals (ODIs)?",
            "options": ["A. Sachin Tendulkar", "B. Rohit Sharma", "C. Virat Kohli", "D. Chris Gayle"],
            "answer": "B"
        },
        {
            "question": "14.Which country won the ICC Cricket World Cup in 2019?",
            "options": ["A. Australia", "B. India", "C. England", "D. New Zealand"],
            "answer": "C"
        },
        {
            "question": "15.Who is known as the father of modern physics?",
            "options": ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"],
            "answer": "B"
        },
        {
            "question": "16.Who discovered penicillin?",
            "options": ["A. Alexander Fleming", "B. Louis Pasteur", "C. Marie Curie", "D. Thomas Edison"],
            "answer": "A"
        },
        {
            "question": "17.Which Bollywood film won the Best Picture award at the Oscars in 2009?",
            "options": ["A. Lagaan", "B. Slumdog Millionaire", "C. Bajrangi Bhaijaan", "D. 3 Idiots"],
            "answer": "B"
        },
        {
            "question": "18.Who is the director of the Bollywood movie 'Dangal'?",
            "options": ["A. Karan Johar", "B. Aamir Khan", "C. Rajkumar Hirani", "D. Nitesh Tiwari"],
            "answer": "D"
        },
        {
            "question": "19.Which actor played the role of Tony Stark/Iron Man in the Marvel Cinematic Universe?",
            "options": ["A. Robert Downey Jr.", "B. Chris Evans", "C. Chris Hemsworth", "D. Mark Ruffalo"],
            "answer": "A"
        },
        {
            "question": "20.Who directed the movie 'Inception'?",
            "options": ["A. Christopher Nolan", "B. Steven Spielberg", "C. Quentin Tarantino", "D. Martin Scorsese"],
            "answer": "A"
        }
    
]

# Call the KBC_p function to start the game
KBC_p()
sys.exit()
