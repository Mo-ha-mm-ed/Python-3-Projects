##########################################################################################
#
#   This program was design as Magic 8-Ball. Where the uesrs ask a yes/no questions  
#       Then the program will generate random answer for users' question.
#           The process is done on 4 stages.
# 
#           
# 
#
##########################################################################################
# Here we identify and import some libraries and tools
import random
import re

verbs_in_yes_or_no_question = ["Does", "Will", "Is", "Have", "Could", "Should", "Did", "Would","Do", "Am", "Should", "Had", "Can", "Were", "Shall", "May", "Might", "Must", "Are"]

#Yes or no question pattern
pattern = r"^(?:%s) .*[\?\.!]*$" % '|'.join(verbs_in_yes_or_no_question)



##########################################################################################
#stage 1 (Starting the program)
stage_one = True
while stage_one:
    print(" ")
    get_the_name_of_the_user = input("Hello, What is your name? ")
    print(" ")
    
    # Validate user entry. Only words. No other charachters allowed such as false or true
    if get_the_name_of_the_user.isalpha() == True:
        get_the_name_of_the_user = get_the_name_of_the_user.capitalize()
        
        #Validate if user enters word that can cause a problem such as False 
        # or True in username.
        if get_the_name_of_the_user == "False":
            print(" ")
            print("Using False is invalid entry")
            print(" ")
        elif get_the_name_of_the_user == "True":
            print(" ")
            print("Using True is invalid entry")
            print(" ")
        #Validate if name is less than 3 charachters  
        elif len(get_the_name_of_the_user) < 3: 
            print(" ")
            print("Please enter a name that is more than 3 letters")
            print(" ")
        
   
        # Validation of username is success, then we enter stage 2  
        else:
            #######   Stage 2  ##########
            ###### user question ######
            stage_two = True
            while stage_two:
                print(" ")
                get_user_question = input("What is your question? ")
                print(" ")
                
                #Validate user question. Only words, no numbers, no less than 7 charachter.
                if all(c.isalpha() or c.isspace() or c == '?' for c in get_user_question):
                    get_user_question = get_user_question.capitalize()
                    
                    #Validate if user enters word that can cause a problem such as False 
                    # or True in question.
                    if get_user_question == "False":
                        print(" ")
                        print("Using False is invalid entry")
                        print(" ")
                        
                    elif get_user_question == "True":
                        print(" ")
                        print("Using True is invalid entry")
                        print(" ")
                    
                    # Validate if user enters a question less than 7 charachters.
                    elif len(get_user_question) < 7:
                        print(" ")
                        print("Please enter a question that is more than 7 letters")
                        print(" ")
                    
                    ##### Finaly Check if question provided is yes/no question.
                    else:
                        ## Yes/No question pattern
                        pattern = r"^(?:%s) .*[\?\.!]*$" % '|'.join(verbs_in_yes_or_no_question)
                        if re.match(pattern, get_user_question, re.IGNORECASE):
                            print(" ")
                            print(" ")
                            #######   Success, Now return answer  ##########
                            #######   Stage 3  (Answer the question)##########
                            print("Hello " + get_the_name_of_the_user)
                            print(" ")
                            ## generate random number, then return random answer
                            random_number = random.randint(1, 9)
                            
                            if random_number == 1:
                                answer = "Yes - definitely"
                                print(" ")
                                print("Your question is " + get_user_question)
                                print(", and Msgic 8-Ball answer: " + answer)
                                print(" ")
                            
                            elif random_number == 2:
                                answer = "It is decidedly so"
                                print(" ")
                                print("Your question is " + get_user_question)
                                print(", and Msgic 8-Ball answer: " + answer)
                                print(" ")
                            
                            elif random_number == 3:
                                answer = "Without a doubt"
                                print(" ")
                                print("Your question is " + get_user_question)
                                print(", and Msgic 8-Ball answer: " + answer)
                                print(" ")
                            
                            elif random_number == 4:
                                answer = "Reply hazy, try again"
                                print(" ")
                                print("Your question is " + get_user_question)
                                print(", and Msgic 8-Ball answer: " + answer)
                                print(" ")
                            
                            elif random_number == 5:
                                answer = "Ask again later"
                                print(" ")
                                print("Your question is " + get_user_question)
                                print(", and Msgic 8-Ball answer: " + answer)
                                print(" ")
                            
                            elif random_number == 6:
                                answer = "Better not tell you now"
                                print(" ")
                                print("Your question is " + get_user_question)
                                print(", and Msgic 8-Ball answer: " + answer)
                                print(" ")
                            
                            elif random_number == 7:
                                answer = "My sources say no"
                                print(" ")
                                print("Your question is " + get_user_question)
                                print(", and Msgic 8-Ball answer: " + answer)
                                print(" ")
                            
                            elif random_number == 8:
                                answer = "Outlook not so good"
                                print(" ")
                                print("Your question is " + get_user_question)
                                print(", and Msgic 8-Ball answer: " + answer)
                                print(" ")
                            
                            elif random_number == 9:
                                answer = "Very doubtful"
                                print(" ")
                                print("Your question is " + get_user_question)
                                print(", and Msgic 8-Ball answer: " + answer) 
                                print(" ")
                            
                            #######   Stage 4 (Final Stage. Check if user has another question or exit the program) ##########
                            stage_four = True
                            while stage_four:
                                print(" ")
                                print("Would you like to ask another question or restart the program?")
                                print(" ")
                                print("Please only enter the number of the choice you wish")
                                print("1)Ask another question")
                                print("2)Exit the program")
                                print(" ")
                                ask_user_to_end_or_continue = input("==> ")
                                
                                # Check if user entry is numbers only
                                if ask_user_to_end_or_continue.isdigit() == True:
                                    #convert number to integer to check it
                                    ask_user_to_end_or_continue = int(ask_user_to_end_or_continue)
                                    if ask_user_to_end_or_continue == 1:
                                        print(" ")
                                        break #ask new question
                                    
                                    elif ask_user_to_end_or_continue == 2:
                                        print("Goodbye...")
                                        print(" ")
                                        exit() #exit the program
                                    
                                    # If user enter any other number that is not 1 or 2.
                                    else: 
                                        print(" ")
                                        ask_user_to_end_or_continue = str(ask_user_to_end_or_continue)
                                        print(ask_user_to_end_or_continue + " is not a valid entry")
                                        print(" ")
                                        
                                # If user did not enter number, then this respond should appear
                                else:
                                    print("Only 1 or 2 is allowed as input")
                                    print(" ")
                        
                        # If question provided is not yes/no question  
                        else:
                            print(" ")
                            print("You should only add yes or no question. What you provided is not Yes or no question")
                            print(" ")

                # if user uses numbers or amy other charachters
                else:
                    print(" ")
                    print("Invalid question")
                    print("Words are only accepted")
                    print(" ")
                    
    # If user added invalid input for username.
    else:
        print(" ")
        print("Invalid username. Username should not be more than one word,")
        print("No special charachter or space or numbers are allowed")
        print("Also, user entry should be no less than 3 letters")
        print(" ")
        
##########################################################################################