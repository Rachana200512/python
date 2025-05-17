#riddles game
print("Welcome to the riddle quiz")

questions = ("What is always infront of you but cannot be seen?",
    "What goes up but never comes down?" ,
    "Where does today come  before yesterday?" ,
    "What has words,but never speaks?",
    "What two things can you never eat before breakfast?",
    "The more you take, the more you leave behind. What am I?",
    "I am an odd number. Take away a letter and I become even. What number am I?",
    "What is at the end of a rainbow?",
    "What goes through cities and fields, but never moves?",
    "I have no life, but I can die. What am I?",
    "What kind of room has no walls, door or windows?",
    "What can travel all around the world without leaving its corner?",
    "What starts with a T, ends with a T, and has T in it?",
    "What begins with an “e” and only contains one letter?",
    "Which month has 28 days?"
     )

answers = (  "future",
           "age",
           "dictionary",
            "book",
            "lunch and dinner",
            "footsteps",
            "seven",
            "w",
            "road",
            "battery",
            "mushroom",
            "stamp",
            "teapot",
            "envelope",
            "every month"
            )

guess = []
score = 0
question_number = 0

for question in questions:
    print("*********************************")
    print(question)

    user_guess = input("Enter your answer:").lower() .strip()
    guess.append(user_guess)
    if user_guess == answers[question_number]:
     score +=1
     print("correct🎉")
    
    else:
     print("Incorrect😓")
     print(f"the correct answer is {answers[question_number]}")
    question_number += 1
score = ((score / len(questions)) *100)
print("your final score is ",score %.2f)