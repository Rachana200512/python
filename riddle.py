#riddles game
print("Welcome to the riddle quiz")

questions = ("What is always infront of you but cannot be seen?",
    "What goes up but never comes down?" ,
    "Where does today come  before yesterday?" ,
    "What has words,but never speaks?",
    "What two things can you never eat before breakfast?")

answers = (  "future",
           "age",
           "in dictionary",
            "book",
            "lunch and dinner")

guess = []
score = 0
question_number = 0

for question in questions:
    print("*********************************")
    print(question)

    user_guess = input("Enter your answer:")
    guess.append(user_guess)
    if user_guess == answers[question_number]:
     score +=1
     print("correct🎉")
    
    else:
     print("Incorrect😓")
     print(f"the correct answer is {answers[question_number]}")
    question_number += 1
score = ((score / len(questions)) *100)
print("your final score is ",score)