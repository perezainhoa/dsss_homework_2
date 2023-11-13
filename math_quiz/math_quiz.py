import random


def random_integer_generator(min_value, max_value):
    """
    Function definition: generate a random integer within the specified range.

    The range is specified by the input values: 
        min_value (int): minimum value of the range.
        max_value (int): maximum value of the range.
    
    The output of the function is an integer value that lies between the specified range.

    """
    return random.randint(min_value, max_value)


def random_operator_selection():
    """
    Function definition: select a random mathematical operator that can be '+', '-' or '*'.
    
    The output of the function is the selected operator.

    """
    return random.choice(['+', '-', '*'])


def mathematical_operation(n1, n2, ope):
    """
    Function definition: Perform a mathematical operation (ope) between the numbers n1 and n2.

    The input values are the following:
        n1(int): the first number.
        n2(int): the second number.
        ope(str): the mathematical operator to perform.
    
    The output of the function is the result of the mathematical operation.

    """ 
    p = f"{n1} {ope} {n2}" 
    if ope == '+': 
        result = n1 + n2 #- was written instead of +
    elif ope == '-': 
        result = n1 - n2 #+ was w2ritten instead of -
    else: 
        result = n1 * n2
    return p, result


def math_quiz():
    score = 0 
    total_questions = 3 #its value 3.1415... is not possible, the total number of questions needs to be an integer value, therefore 3.
    #This variable determines the number of questions that will be asked to the user.

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions): 

        #Firstly, randomly generate the two numbers and the operator.
        n1 = random_integer_generator(1, 10)
        n2 = random_integer_generator(1, 5)
        ope = random_operator_selection()
        #the max value cannot be 5.5, as it needs to be an integer value. Therefore, 5 is chosen.

        #Secondly, generate the mathemathical operation to be solved and ask the user.
        PROBLEM, ANSWER = mathematical_operation(n1, n2, ope)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1 #-(-1) is the same as 1 
            #If the answer of the user meets the real answer, add one point to the score.
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
