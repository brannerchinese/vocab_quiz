#!/usr/bin/env python
# This program is a fill-in-the blank quiz, prompting for user input at each blank.

import os

#These variables contain quiz questions and answers for each difficulty level
easy_questions = ["___1___ is a popular programming language that boasts high-readability code. You might think it was named after a snake species, but it was actually named after a British comedy act.", "The python interpreter can interpret and manipulate various types of data. A whole number is referred to as an ___2___, while a decimal is known as a float. ", "Another data type is called a ___3___. It can contain letters, words, sentences, or other characters saved as text. ", "Another useful data type in python is a ___4___, which stores a sequence of values separated by commas."]
easy_answers = ["python", "integer", "string", "list"]


medium_questions = ["One of the first steps when learning to code is to learn how to assign a value to a ___1___, which then stores that value in the computer's memory. ", "Next you will probably want to learn how to use simple ___2___s such as +, -, *, /, >, <, ==, and !=. ", "Once you've mastered variables and operators, it's time to start learning how to write some simple ___3___s (aka functions), which consist of lines of code that run in a specified order and can eliminate redundancy. ", "A procedure takes one or more ___4___s as arguments, and returns one or more outputs."]
medium_answers = ["variable", "operator", "procedure", "input"]

hard_questions = ["One important programming construct is called an ___1___ statement; it tests whether a condition is true, and if so it may execute a block of code. ", "Another important construct used especially when writing procedures is a ___2___, which allows you to keep running the same code repeatedly under specified conditions. ", "There are two common types of these repeating operations; one is called a ___3___ loop; it runs through all of the values in a specified range. ", "The other is called a ___4___ loop; this one runs repeatedly as long as a specified condition is true. "]
hard_answers = ["if", "loop", "for", "while"]

def evaluate(user_input, correct_answer):
#procedure that evaluates user response
	if user_input.lower() == correct_answer:
		return True
	return False	


def replace_blank(index, question, correct_answer):
#procedure that replaces the blank with the correct answer
        blank = "{0}{1}{0}".format("___", str(index + 1))
        filled_question = question.replace(blank, correct_answer)
        capitalized_question = filled_question.upper()[0] + filled_question[1:]
        return capitalized_question

def quiz_summary(errors):
#print out a final message at the end of the quiz
        accuracy = '{0:.2f}'.format(4.0/(errors + 4) * 100)
        print "{} {} {}".format("\nCongratulations! You survived the quiz. Your accurracy was", 
                accuracy, "percent.\n")
        last_input = raw_input("How was your experience? ")
        print "{} {} {}".format("\nGlad to hear it was", last_input.lower(), ". See you later!")

def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

def run_quiz():
        clear_terminal()
        print "Welcome to the quiz!"

        #difficulty is set through user input
        difficulty = raw_input("\nTo select the difficulty setting, please enter easy, medium, or hard: ")
        while difficulty not in ["easy", "medium", "hard"]:
                difficulty = raw_input("Please enter a valid difficulty level: ")

        #variables are assigned values depending on the selected difficulty
        level = {"easy": (easy_questions, easy_answers), "medium": (medium_questions, medium_answers), "hard": (hard_questions, hard_answers)}
        questions, answers = level[difficulty]

        #questions are printed out and index, score, and errors are initialized
        index = 0
        score = 0
        errors = 0

        clear_terminal()

        while index < 4:
                print "{0} {1} {2}{2}{3}".format("Question", str(index + 1), "\n", questions[index])

                #appropriate prompt for response printed based on index
                user_input = raw_input("\nType the answer for question " + str(index + 1) + ": ")

                if evaluate(user_input, answers[index]):
                        score += 1	
                        print "\n\n\n\n\nGreat!\n\n" + replace_blank(index, questions[index], answers[index]) + "\n\nYour score is " + str(score)
                        index += 1
                        raw_input("\nPress enter to continue")
                        clear_terminal()
                else:
                        errors += 1
                        print "\nNope! Try again."

        quiz_summary(errors)

run_quiz()
