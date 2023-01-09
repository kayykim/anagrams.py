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
                easy_letters = random_letters(3,5)

                print (easy_letters)
                return (easy_letters)

               
            #If the level is 2, it will display a set of 7 random letters
            
            elif level == 2:
                print()
                print("Your letters are: ")
                #insert letters here!!!
                mid_letters = random_letters(3,4)
                
                print (mid_letters)
                return mid_letters


            #If the level is 3, it will display a set of 6 random letters
            
            elif level == 3:
                print()
                print("Your letters are: ")
                #insert letters here!!!
                hard_letters = random_letters(2,4)

                print(hard_letters)
                return hard_letters


            #If the user wants to leave the game before starting
            
            if level == 4:
                leave = ()

                #Double check that the user did not accidentally select wrong input
                while leave != "Y" and leave != "N":
                    leave = input("Are you sure you want to quit,(Y) yes (N) no?: ")
                    leave = leave.upper()
                    

                #If they want to leave, code returns to the main program
                    
                    if leave == "Y" :
                        return "N"


                #If they don't want to leave print global variable letters
                
                    else:
                        print(letters)
                 
            break

        except:
            print()
            print("Please enter a number between 1-4")
            print()

# random_letters function displays letters based on difficulty chosen
# This has two parameters to make sure enough vowels are included.

def random_letters (num_v, num_c):
    import random
    

    #Create seperate lists for both vowels and consanants
    #Some letters are included more than once since they are most common
    
    vowels = ["A", "A", "A", "E", "E", "E", "I", "I", "I", "O", "O",
              "O", "U"]
    consanants = ["B", "C", "D", "F", "G", "H", "H", "J", "K", "L",
                  "M", "N", "N", "P", "Q", "R", "R", "S", "S", "S",
                  "T", "T", "V", "W", "Y", "Z"]
    alist = []
    blist = []
    

    #Get n number of random vowels and put them in a list
    
    for y in range (num_v):
        v = random.choice(vowels)
        alist.append(v)


    #Get n number of random consanants and put them in a list
        
    for z in range (num_c):
        c = random.choice(consanants)
        blist.append(c)


    #Add the two previous lists together and return it to the main program
        
    final_list = alist + blist
    return final_list


# valid_word takes the inputted word from user and 
# 1. checks if it's is in the list of words, 2. already used, 3. accumulates points

def valid_word():

    #make a list to keep track of user's word's used
    
    words_used = []
    print (" ")
    
    leave = ()

    words_used = []

    point = 0
    total_points = 0
    

    # User repeatly inputs word until sentinel is met

    while leave != "!":
                
        user = input ("Enter a word: ")
        user = user.upper()
                
                
        # User's word gets seperated into a list
        
        length_word = len(user)
        value = 0
                
        for x in (user):
            num = x

            # Make sure user did not use the same word
            
            if num in letters:
                value += 1

            else:
                value += 0
                
        user = (user + "\n").lower()
        
        # Conditions to be met for user inputted word to be valid.
        
        if user in content_list[:] and user not in words_used and \
           value== length_word and value > 2:            
            point += 1
            print ("Point:",point)

                    
            #store what user entered into the list
            
            words_used.append(user)



        # If the word is not valid
        
        else:
            print ("Not a valid word")


        # Ask if the user wants to quit or continue

        leave = input ("Enter \'!\' if you want to quit, "\
                       "\'ENTER\' if you want to continue: ")
        print (" ")


    # Display the user's total points

    print ("Well Played!")
    print ("Your total points were:", point)
        
# Main program
letters = menu()
valid_word()
