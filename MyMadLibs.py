# -*- coding: utf-8 -*-

#THE HARRY POTTER TRIVIA GAME - REVERSE MAD-LIBS STYLE

#level 1
level1_string = "Harry has his foremost contact with the wizarding world\
 through a half-giant, ___1___ , keeper of grounds and\
 keys at ___2___ . Hagrid reveals some of Harry's history.\
 Harry learns that, as a baby, he witnessed his parents'\
 ___3___ by the power-obsessed dark wizard ___4___ , who\
 subsequently attempted to kill him as well. Harry\
 survived with only a lightning-shaped ___5___ on his\
 forehead as a memento of the attack and Voldemort\
 disappeared soon afterwards. At the orders of the\
 well-known wizard Albus ___6___ , the orphaned Harry\
 had been placed in the home of his unpleasant Muggle\
 relatives, the Dursleys."
                
level1_ans = ["hagrid", "hogwarts", "murder", "voldemort", "scar", "dumbledore"]


#level 2
level2_string = "Just as ___1___ is starting to anticipate his return\
 to ___2___ School, an impish house-elf named ___3___ \
 arrives out of nowhere to warn Harry against the\
 decision to return to the wizarding world, citing\
 grave danger as the reason and inciting Harry’s\
 gravest punishment yet when he smashes a dessert\
 crafted by aunt ___4___ for the dinner party and frames\
 it on ___5___ himself. ___6___ Weasley arrives with his\
 twin brothers Fred and George to perform a jailbreak\
 in their father Arthur’s enchanted car and to\
 deposit him at their family home the Burrow for\
 the remainder of his holidays."

level2_ans = ["harry", "hogwarts", "dobby", "petunia", "harry", "ron"]


#level3
level3_string = "___1___ is back at the Dursleys, where he sees on Muggle\
 television that a prisoner named ___2___ Black has escaped.\
 Harry involuntarily inflates Aunt ___3___ when she comes\
 to visit after she insults Harry and his parents.\
 This leads to his running away and getting picked up by\
 the ___4___ Bus. He travels to ___5___ Alley, where he\
 meets ___6___ Fudge, the Minister for magic, who asks\
 Harry to stay in Diagon Alley for the remaining three weeks\
 before the start of the school year at Hogwarts."

level3_ans = ["harry", "sirius", "marge", "knight", "diagon", "cornelius"]


#level4
level4_string = "The book opens with ___1___ seeing Frank Bryce being killed\
 by Lord ___2___ in a vision, and is awoken by his scar hurting.\
 The Weasleys then take Harry and ___3___ Granger to the\
 ___4___ World Cup, using a Portkey, to watch ___5___ versus\
 Bulgaria, with Ireland emerging victorious. There, Harry meets\
 ___6___  Diggory, who is attending the match with his father."

level4_ans = ["harry", "voldemort", "hermione", "quidditch", "ireland", "cedric"]


#level5
level5_string = "During another summer with his Aunt Petunia and Uncle\
 ___1___ , Harry Potter and ___2___ are attacked by ___3___ .\
 After using magic to save Dudley and himself, Harry is\
 expelled from ___4___ , but the decision is later rescinded.\
 Harry is whisked off by a group of wizards to Number 12,\
 Grimmauld Place, the home of his godfather, ___5___ Black.\
 The house also serves as the headquarters of the Order of\
 the ___6___ , of which Mr. and Mrs. Weasley, Remus Lupin,\
 Mad-Eye Moody, and Sirius are members."

level5_ans = ["vernon", "dudley", "dementors", "hogwarts", "sirius", "phoenix"]


#level6
level6_string = "Dumbledore takes ___1___ to the temporary home of\
 Horace ___2___ , former Potions teacher at ___3___ , and\
 persuades Slughorn to return to teach. Harry is taken to\
 the Burrow, where ___4___ Granger has already arrived. The\
 next morning they get their Ordinary Wizarding Level (O.W.L.)\
 results, along with lists of school supplies. Later, Harry, Ron\
 Weasley and Hermione Granger follow ___5___ Malfoy to Dark Arts\
 supplier Borgin and Burkes. Harry is instantly suspicious of\
 Draco, whom he believes to be a ___6___ Eater."

level6_ans = ["harry", "slughorn", "hogwarts", "hermione", "draco", "death"]


#level7
level7_string = "Abandoning school, ___1___ and Hermione accompany Harry to\
 finish the quest of Dumbledore to hunt and destroy the four\
 remaining ___2___ of Voldemort. Initially they have very few\
 clues — one is a locket once owned by the co-founder of Hogwarts,\
 Salazar ___3___ which was stolen by the mysterious R.A.B.,\
 one is possibly a cup originally belonging to co-founder\
 Helga ___4___ , a third might be connected to co-founder\
 Rowena ___5___ , and the fourth might be ___6___ , the snake\
 of Lord Voldemort."

level7_ans = ["ron", "horcruxes", "slytherin", "hufflepuff", "ravenclaw", "nagini"]


def word_in_pos(testword, correct_answers):
    
    #this function checks if the answer
    #supplied by the user is in the
    #answer list of the level or not.
    #It will return the answer if correct,
    #otherwise, it will return None
    
    for pos in correct_answers:
        if pos == testword:
            return pos
    return None


def select_level(level_num):
    
    #this function allows the user
    #to select the level he/she wants
    #to play. If the level number
    #entered is invalid, it prompts
    #the user to enter the level
    #number again. It returns the
    #question string and the list of
    #correct answers of the level
    #selected by the user.
    
    if level_num == "1":
        return level1_ans, level1_string

    elif level_num == "2":
        return level2_ans, level2_string

    elif level_num == "3":
        return level3_ans, level3_string

    elif level_num == "4":
        return level4_ans, level4_string

    elif level_num == "5":
        return level5_ans, level5_string

    elif level_num == "6":
        return level6_ans, level6_string

    elif level_num == "7":
        return level7_ans, level7_string

    else:
        print "Please enter a valid level number ! \n"
        level_num = raw_input("\nType in the number of the level you want a quiz on: ")
        return select_level(level_num)


def answer_check(level_canswer, level_string):

    #This function executed the selected level.
    #This function checks if the answer filled
    #in by the user for the blank is correct or
    #not and runs till the user has cleared the
    #selected level. The inputs are the correct
    #answer string of the level and the question
    #string. It does not return anything.
    #level_canswer identifies the list of correct
    #answers for that level.
    
    i = 0
    
    while i < len(level_canswer):
        user_answer = raw_input("\n \nWhat is your answer for blank " + str(i + 1) + "? \n")

        if word_in_pos(user_answer, level_canswer) != None:
            
            if level_canswer[i] == user_answer:
                level_string = level_string.split()
                temp = level_string.index("___" + str(i + 1) + "___")
                word = level_string[temp]
                word = word.replace("___" + str(i + 1) + "___" , user_answer)
                level_string[temp] = word

                i += 1

                print "\nCorrect Answer !\n"
                level_string = " ".join(level_string)
                print level_string

        else:
                print "\nWrong answer. Try again!\n"
                print level_string

    print "\n \n" + "*" * 20 + "Fantastic! LEVEL CLEARED!" + "*" * 20 + "\n \n"
    return                                      
                                           

def play_game():

       #This function executes the trivia game
       #by asking the user which level he/she
       #wants to play. When a level is cleared,
       #it again asks the user if he/she wants to
       #play again or not.

       choice = "yes"

       while choice == "yes":

             print "*" * 20 + "WELCOME TO THE HARRY POTTER TRIVIA GAME !" + "*" * 20 + "\n \n"
             print "\n 1. Harry Potter and the Sorcerer's Stone  (Easy)\n"
             print "\n 2. Harry Potter and the Chamber of Secrets  (Easy)\n"
             print "\n 3. Harry Potter and the Prisoner of Azkaban  (Medium)\n"
             print "\n 4. Harry Potter and the Goblet of Fire  (Medium)\n"
             print "\n 5. Harry Potter and the Order of the Phoenix  (Hard)\n"
             print "\n 6. Harry Potter and the Half-Blood Prince  (Medium)\n"
             print "\n 7. Harry Potter and the Deathly Hallows  (Hard)\n"

             print "\n \n" + "*" * 20 + "Answer all questions in lowercase letters" + "*" * 20 + "\n \n"

             level_number = raw_input("Type the number of the Harry Potter book you want to play the trivia quiz of: ")
             print "\n \n"

             level_canswer, level_string = select_level(level_number)
             
             print level_string + " \n \n"
             answer_check(level_canswer, level_string)

             choice = raw_input("Do you want to play the trivia quiz for another level? (yes/no)\n")
             print "\n \n"

       print "Thank you !"

#LET'S START THE GAME !!                                              
play_game()                                        
                                          
                                
    
    
    
                


                








    
         
        
