# Create a function to start quiz 1 with no arguments.
def gen1_questions_ans():
    # Each question is given a global variable to initialize in each function.
    global q1, q2, q3, q4, q5, q6, q7, q8, q9, q10
    score = 0   # Variable to initialize the score to zero at the start of every game

    '''
    You are first asked the questions for the quiz that you have chosen. The inputs are not case sensitive because of
    .lower(). If the anwer you type is correct then you will be notified it is correct and one point will be added to
    your score. If anything else is typed then you are notified that your answer is incorrect. Your cumulative score 
    is then assigned the variable high_score. You are then given a congratulations message along with your total score.
    '''

    q1 = input("Question 1. What is the rarest M&M color? ")
    if q1.lower() == "brown":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    q2 = input(
        "Question 2. In a website browser address bar, what does “www” stand for? ")
    if q2.lower() == "world wide web":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    q3 = input(
        "Question 3. Which country consumes the most chocolate per capita? ")
    if q3.lower() == "switzerland":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    q4 = input("Question 4. Who was the very first American Idol winner? ")
    if q4.lower() == "kelly clarkson":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    q5 = input(
        "Question 5. What is the tiny piece at the end of a shoelace called? ")
    if q5.lower() == "aglet":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    q6 = input("Question 6. How many weeks are in a year? ")
    if q6.lower() == "52":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    q7 = input("Question 7. Which animal can be seen on the Porsche logo? ")
    if q7.lower() == "horse":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    q8 = input("Question 8. Muhammad Ali was well-known in which sport? ")
    if q8.lower() == "boxing":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    q9 = input("Question 9. What is the lowest army rank of a US soldier? ")
    if q9.lower() == "private":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    q10 = input(
        "Question 10. What is often seen as the smallest unit of memory greater than a byte? ")
    if q10.lower() == "kilobyte":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")

    high_score = score

    print("\n***Congratulations on finishing the game.***\nYou have scored",
          high_score, "points!")


# Create a function to start quiz 2 with no arguments.
def gen2_questions_ans():
    # Each question is given a global variable to initialize in each function.
    global q1, q2, q3, q4, q5, q6, q7, q8, q9, q10
    score = 0   # Variable to initialize the score to zero at the start of every game
    q1 = input(
        "Question 1. Which is one of two U.S. states does not observe Daylight Saving Time? ")
    if q1.lower() == "arizona" or q1.lower() == "hawaii":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    q2 = input(
        "Question 2. Michael Jordan won how many NBA titles with the Chicago Bulls? ")
    if q2.lower() == "6":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    q3 = input("Question 3. What color eyes do most humans have? ")
    if q3.lower() == "brown":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    q4 = input("Question 4. What is the hardest rock on earth? ")
    if q4.lower() == "diamond":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    q5 = input("Question 5. What is the solar systems hottest planet? ")
    if q5.lower() == "venus":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    q6 = input("Question 6. What is the fastest-flying bird in the world? ")
    if q6.lower() == "preregrine falcon":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    q7 = input(
        "Question 7. Who was the first woman to have four country albums reach No. 1 on the Billboard 200? ")
    if q7.lower() == "carrie underwood":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    q8 = input(
        "Question 8. What is illegal for a single lady to do in Florida solely on Sundays? ")
    if q8.lower() == "skydive":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    q9 = input("Question 9. Which is the Worlds Largest Ocean? ")
    if q9.lower() == "pacific":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    q10 = input(
        "Question 10. What type of exercise is best for getting the blood flowing? ")
    if q10.lower() == "aerobic":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")

    high_score = score

    print("\n***Congratulations on finishing the game.***\nYou have scored",
          high_score, "points!")
