# store the dictonary in variable: content_list

my_file = open('word.txt', 'r')
content_list = my_file.readlines()

num_of_lists = int(len(content_list))


# Create a function for the instructions of the game

def menu():
    start = ()


    #Get the user to enter START to play the game
    
    while start != "START":
        print ()
        print("WELCOME TO ANAGRAM!")
        start = input("Enter START to play: ")
        start = start.upper()
        print()


    #Display the rules of the game to the user
        
    print ("The rule of the game are as follows: ")
    print()
    print ("You will be given an amount of letters based off of the", end=""
               " difficulty level of your choosing. ")
    print ("You will then have to create as many words as you possibly can")
    print()
    print ("HAVE FUN!")

        
    #The various levels of the game including quiting the game
    
    print()
    print("Enter 1 for easy (8 letters)")
    print("Enter 2 for medium (7 letters)")
    print("Enter 3 for hard (6 letters)")
    print("Enter 4 to QUIT ")
    print()

menu()
