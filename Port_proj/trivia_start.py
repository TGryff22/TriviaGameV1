# importing the questions and answers from another file
from trivia_pkg.trivia_questions_ans import gen1_questions_ans, gen2_questions_ans


# Create a function to show the starting menu with no arguments.
def show_menu():
    # Inout your name for personaliztion
    name = input("Please input your name: ")

    # You are welcomed with a print statement including the variable name for what oyu inputted.
    print("Welcome", name, "to the world's greatest trivia game!!!")

    # A formatted menu is displayed using a print statement.
    print('''
 === Quiz Selection ===   Bo
__________________________
| 1.  General Knowledge 1 |
——————————————————————————
| 2.  General Knowledge 2 | 
——————————————————————————
| 3.  Exit                |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ''')


# Create a function to select your meu option with no arguments.
def topic():
    while True:   # While loop to select what quiz you want if you make the correct choice.
        # User is prompted to input 1, 2, or 3 to make a vaalid selection
        trivia_topic = input(
            "Please select which quiz you would like to take or if you would like to exit the game.\nPlease enter 1, 2, or 3: ")

        # If you select topic 1 then you will be taken to the first quiz and the while loop breaks.
        if trivia_topic == "1":
            gen1_questions_ans()
            break
        # If you select topic 2 then you will be taken to the second quiz and the while loop breaks.
        elif trivia_topic == "2":
            gen2_questions_ans()
            break
        # If you select topic 3 then you will exit the program.
        elif trivia_topic == "3":
            break
        # Or if you type anything else you are taken back to the begining of the loop and given an error message.
        else:
            print("Your selection is invalid.\n")
            continue


# Create a function to display the leaderboard with no arguments.
def leaderboard():
    # Variable for the top six highest scorers
    users = [("Sarah", 6), ("Bao", 9), ("Matt", 2),
             ("Amy", 7), ("Caitlyn", 1), ("Ray", 5)]

    # Sorting the user array
    users.sort(key=lambda a: a[1], reverse=True)

    # # Format the users
    leaderboard = map(lambda user: user[0] + "| " + str(user[1]), users)

    # Print statements to alert you about the other players and show you their scores.
    print("\nSee where you rank among our top scorers:\n")

    print("\n".join(leaderboard))


'''
Call each function in their correct orders so you are first shown the menu, then you select your option and either you 
can exit the game or take one of the quizes. After you take the quiz your score is saved and and you are shown the 
leaderboard for the other users who have played and their scores.
'''

show_menu()

topic()

leaderboard()
