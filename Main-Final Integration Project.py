__author__ = "Minh Nghia Duong"

import random

print("Hey" * 3)
print("Ready to practice math?")


# avoid crash when user enter strange input
def valid_input(prompt):
    got_valid_input = False
    while got_valid_input is False:
        try:
            answer = int(input(prompt))
            got_valid_input = True
        except ValueError:
            print("Invalid input, try again!")
    return answer


# attempt user enter their answer
def attempt(provider_result):
    attempts = 0
    correct_answer = False
    while attempts < 3 and (not correct_answer):
        answer = valid_input("Enter your answer: ")
        if answer == provider_result:
            print("good!")
            correct_answer = True
        else:
            print('try again!')
            attempts += 1
    return correct_answer


def quiz():
    """
    This is the program for practicing math
    """
    score = 0
    time_program_start = 0
    start = True
    while start:
        num1 = random.randint(10, 20)
        num2 = random.randint(1, 9)
        print("what do you to practice? ")
        print("1. Summation")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. I don't want to do any math now!")
        user_input = valid_input("Enter your choice: ")
        if user_input == 1:
            # 1 Plus question
            print("what is: ", num1, "+", num2)
            provider_result = num1 + num2
            answer = attempt(provider_result)
            if answer:
                score += 1
                time_program_start += 1
            else:
                time_program_start += 1

        elif user_input == 2:
            # 2 subtraction question
            print("what is: ", num1, "-", num2)
            provider_result = num1 - num2
            answer = attempt(provider_result)

            if answer:
                score += 1
                time_program_start += 1
            else:
                time_program_start += 1

        elif user_input == 3:
            # 3 multiplication question
            print("what is: ", num1, "*", num2)
            provider_result = num1 * num2
            answer = attempt(provider_result)

            if answer:
                score += 1
                time_program_start += 1
            else:
                time_program_start += 1

        elif user_input == 4:
            # 4 divide question
            print("what is: ", num1, "/", num2)
            provider_result = round(num1 / num2)
            answer = attempt(provider_result)

            if answer:
                score += 1
                time_program_start += 1
            else:
                time_program_start += 1

        elif user_input == 5:
            start = False
    return [score, time_program_start]


""" This is a part to calculate the score and report it"""


# Find the average score
def average(score, time_program_start):
    if time_program_start > 0:
        avg = (score / time_program_start) * 10
    else:
        exit()
    return avg


# find the scale
def scale(score, time_program_start):
    if average(score, time_program_start) > 9:
        status = str("Excellent")
    elif (average(score, time_program_start) <= 9) and (
            average(score, time_program_start) >= 8):
        status = str("Good")
    elif (average(score, time_program_start) < 8) and (
            average(score, time_program_start) >= 7):
        status = str("Accepted")
    else:
        status = str("Fail")
    return status


# tell user what they got.
def plan(score, time_program_start):
    if (average(score, time_program_start) > 9) or (
            average(score, time_program_start) >= 7):
        print("Congratulation!")
    elif not (average(score, time_program_start) > 9) or (
            average(score, time_program_start) >= 7):
        print("Hope you doing better next time!")


""" store user's information and score """


def info(score, time_program_start):
    last_name = input("Enter your last name: ")
    first_name = input("Enter your first name: ")
    student_score = average(score, time_program_start)

    in_file = open("studentInfo.txt", 'w')
    in_file.write("Name: " + first_name + " " + last_name)
    in_file.write("\nYour score:" + str(student_score))
    in_file.write("\n")
    in_file.write(scale(score, time_program_start))
    in_file.write("\n")
    in_file.close()
    print("Data is saved in file: studentInfo.txt")
    print("Open file to see score!")


""" 
main work:
step1: choose the number of student taking test
step 2: run the quiz to get score
step 3 calculate the score on average number question have been taken
step 4: store information and score in file txt 
"""


def main():
    student_test = valid_input("Enter number of student taking test: ")
    for number_student_test in range(student_test):
        score, time_program_start = quiz()
        average(score, time_program_start)
        scale(score, time_program_start)
        plan(score, time_program_start)
        info(score, time_program_start)


if __name__ == "__main__":
    main()

# https://note.nkmk.me/en/python-function-return-multiple-values/
# https://github.com/mduong7281/mduong7281.main.github.io
