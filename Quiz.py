# A dictionay that stores qst and answer
# A variable that tracks the score of the user
# Loop through the dictionary useing the key value  pairs

# Display each question to the user and allow then to answer
# Tell them if they are right or wrong

# Show the final score to the user when complete

quiz = {
    "question1":{
        "question":"What is the capital of France",
        "answer" :"paris"},
    "question2":{
        "question":" What is the capital of Germany",
        "answer": "Berlin"},
    "question3":{
        "question":"What is the capital of Itly",
        "answer": "Rome"},
    "question4":{
        "question":"What is the capital of Portugal",
        "answer": "Lisbon"},
    "question5":{
        "question":"What is the capital of spain ",
        "answer": "Madrid"},
    }

score = 0
for key ,value in quiz.items():
    print(value['question'])
    answer = input("Answer?")
    
    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("your score is " + str(score))
    else:
        print("Wrong answer")
        print("The correct answer is " + value ['answer'])
        print("Your score is : " + str(score))

print("Your percentage is :" + str(int((score /7)*100))+ "%")
    
    