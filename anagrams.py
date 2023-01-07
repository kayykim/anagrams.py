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
    
    #Error check user input of the level using try/except 
    
    while True:
        try:
            level = int(input("Enter difficulty level: "))


            #The entered level needs to be between 1 and 4
            
            if level < 1 or level > 4:
                print("error")


            #If the level is 1, it will display a set of 8 random letters
                
            if level == 1:
                print()
                print("Your letters are: ")
                #insert letters here!!!
                easy_letters = "easy random letters"

                print (easy_letters)
                return (easy_letters)

               
            #If the level is 2, it will display a set of 7 random letters
            
            elif level == 2:
                print()
                print("Your letters are: ")
                #insert letters here!!!
                mid_letters = "medium random letters"
                
                print (mid_letters)
                return mid_letters


            #If the level is 3, it will display a set of 6 random letters
            
            elif level == 3:
                print()
                print("Your letters are: ")
                #insert letters here!!!
                hard_letters = "hard random letters"

                print(hard_letters)
                return hard_letters


            #If the user wants to leave the game before starting
            
            if level == 4:
                leave = ()

                #Double check that the user did not accidentally select wrong input
                #to do later!!!

        except:
            print()
            print("Please enter a number between 1-4")
            print()


menu()
