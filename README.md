📝 Riddle Quiz - Simple Documentation
📌 Description
This Python program is a riddle quiz game. It asks the user 5 riddle questions, checks the answers, and gives a final score based on how many correct answers were given.

🔧 How the Code Works
1. Prints a Welcome Message
 
print("Welcome to the riddle quiz")
Displays a welcome message to the user when the game starts.

2. Stores Questions and Answers

questions = ( ... )
answers = ( ... )
questions: A tuple containing 5 riddles.
answers: A tuple with the correct answers, matching the question order.

3. Initial Setup
 
guess = []
score = 0
question_number = 0
guess: A list to store the user's answers.
score: Tracks the number of correct answers.
question_number: Keeps track of which question is being asked.

4. Loop Through Questions
 
for question in questions:
    ...
Shows each question to the user.
Gets user input with input().
Compares the user's answer with the correct one using if user_guess == answers[question_number].
Updates the score if the answer is correct.
Shows whether the answer was correct or not.

5. Final Score Calculation
 
score = ((score / len(questions)) * 100)
print("your final score is ", score)
Calculates the percentage of correct answers.
Displays the final score to the user.

✅ Example Output
  
Welcome to the riddle quiz
*********************************
What goes up but never comes down?
Enter your answer: age
correct🎉
...
your final score is 80.0


 





 
