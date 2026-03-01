""" Moulaye Adama Sidibe
November 14th 2025
Throbac_functional
 
 --------------------------------------------------------------------------------------------------------------------------------
 
 """



roman_numerals = ["I","V","X","L","C","D","M"] 
values = [1,5,10,50,100,500,1000]

def roman_to_integer(roman_numeral):
    #parameter - roman_numeral is a string with valid Roman Letters 
    #return - integer > 0 and < 4000

    integer = 0
    index_roman_numeral = 0
    while index_roman_numeral < len(roman_numeral):
        current_ch_integer = values[roman_numerals.index(roman_numeral[index_roman_numeral])]# this line will take the index of ch and look for the correspond value in the list values and add to the total.
        if index_roman_numeral + 1 < len(roman_numeral):
            next_ch_integer = values[roman_numerals.index(roman_numeral[index_roman_numeral + 1])]
            if current_ch_integer >= next_ch_integer:
                integer += current_ch_integer
                index_roman_numeral += 1 #this line is going to take the next_ch_integer 
            else:
                integer += next_ch_integer - current_ch_integer
                index_roman_numeral += 2 #this line is going to take the character after the next_ch_integer
        else:
            integer += current_ch_integer
            index_roman_numeral += 1
    if integer > 3999 or integer <= 0:
        print("The Roman Number you have entered  is OUT OF RANGE")
    else:
        print(f"Value of {roman_numeral}: {integer}")
    return integer
 

def check_roman_letters_validity(roman):
    #parameter - roman is a string with valid Roman Letters 
    #return - Boolean (True or False) if roman numeral character are in roman_numerals (list of valid roman characters)

    for i in range(len(roman)):
        if roman[i] not in roman_numerals:
            return False
    else:
        return True
def check_repetition_validity(roman): # Check repetition rules
    #parameter - roman_numeral is a string with valid Roman Letters 
    #return - Boolean (True or False) if the repetition rules are respected or not 

    if "IIII" in roman or "XXXX" in roman or "CCCC" in roman or "MMMM" in roman:
        return False
    if "VV" in roman or "LL" in roman or "DD" in roman:
        return False
    else:
        return True

def check_subtractive_validity(roman):
    #parameter - roman_numeral is a string with valid Roman Letters 
    #return - Boolean (True or False) if the subtraction rules between the character and the previous one is respected or not


    allowed = ["IV", "IX", "XL", "XC", "CD", "CM"]
    for i in range(len(roman) - 1):
        current = roman[i]
        next_char = roman[i + 1]
        pair = current + next_char
        # If smaller before larger, must be an allowed pair
        if values[roman_numerals.index(current)] < values[roman_numerals.index(next_char)]:
            if pair not in allowed:
                return False
    return True



def get_two_romans():
    #parameter - no parameter. Variables will be defined in the function and ask again to the user until valid roman numerals are entered.
    #return - integer1 and integer2 that are th roman_numerals 1 and 2 converted to integers in the range 1 and 3999 both included.

    roman_numeral1 = input("Enter first Roman Number(no spaces):").upper().strip()

    while not check_roman_letters_validity(roman_numeral1):
        print("Oops. Invalid Roman numeral(s) for the first one. Try again.")
        roman_numeral1 = input("Please enter a valid first Roman Number(no spaces):").upper().strip()

    while not check_repetition_validity(roman_numeral1):
        print("Oops. Invalid Roman numeral(s) repetition for the first one! Try again.")
        roman_numeral1 = input("Please enter a valid first Roman Number(no spaces):").upper().strip()
    while not check_subtractive_validity(roman_numeral1):
        print("Oops. Invalid subtractive form(s) for the first one. Try again.")
        roman_numeral1 = input("Please enter a valid first Roman Number(no spaces):").upper().strip()
    integer1 = roman_to_integer(roman_numeral1)
    
    roman_numeral2 = input("Enter second Roman Number(no spaces):").upper().strip()
    
    while not check_roman_letters_validity(roman_numeral2):
        print("Oops. Invalid Roman numeral(s) for the second one. Try again.")
        roman_numeral2 = input("Please enter a valid second Roman Number(no spaces):").upper().strip()
    
    while not check_repetition_validity(roman_numeral2):
        print("Oops. Invalid Roman numeral(s) repetition for the second one! Try again.")
        roman_numeral2 = input("Please enter a valid second Roman Number(no spaces):").upper().strip()
    while not check_subtractive_validity(roman_numeral2):
        print("Oops. Invalid subtractive form(s) for the second one. Try again.")
        roman_numeral2 = input("Invalid subtractive form.Please enter a valid second Roman Number(no spaces):").upper().strip()   

    integer2 = roman_to_integer(roman_numeral2)
    return integer1, integer2



def check_operator_validity(op):
    #parameter - operator (+,-,/,^,*)
    #return - Boolean (True or False) if the operator is a valid one or not. 


    if op in ["+", "-", "*", "/", "^"]:
        return True
    else:
        return False


def get_operator():
    #parameter - no parameter. Variable is called in the function with comments using as instructions for the user.
    #return - the operator that should be a valid one: "+", "-", "*", "/", "^". 


    operator = input("Enter an operator(+,-,/,^,*):").strip()
    while not check_operator_validity(operator):
        print("Invalid operator! Please enter one of +, -, *, /, ^.")
        operator = input("Please enter a valid operator(+,-,*,/,^):").strip()
    return operator
def addition(a,b):
     #parameter - 2 integers a and b (both between 1 and 3999 included) that will be the 2 roman numerals convert to integers to do the arithmetic.
    #return - the operator (+) and the result of the addition in the range 1 and 3999 both included.  
    operator = "+"
    result = a + b
    if result < 1 or result > 3999:
        print("Operator:", operator)
        print("The digital sum is OUT OF RANGE")
    else:
        print("Operator:", operator)
        print("Digital sum is:", result)
    return (result, operator)

def subtraction(a,b):
    #parameter - 2 integers a and b (both between 1 and 3999 included) that will be the 2 roman numerals convert to integers to do the arithmetic.
    #return - the operator (-) and the absolute value of the result (because we don't want any negative numbers) of the subtraction in the range 1 and 3999 both included. 
    operator = "-"
    result = abs(a - b)
    if result < 1 or result > 3999:
        print("Operator:", operator)
        print("The digital difference is OUT OF RANGE")
    else:
        print("Operator:", operator)
        print("Digital difference is:", result)
    return (result, operator)
def multiplication(a,b):
    #parameter - 2 integers a and b (both between 1 and 3999 included) that will be the 2 roman numerals convert to integers to do the arithmetic.
    #return - the operator (*) and the result of the multiplication in the range 1 and 3999 both included. 

    operator = "*"
    result = a * b
    if result < 1 or result > 3999:
        print("Operator:", operator)
        print("The digital product is OUT OF RANGE")
    else:
        print("Operator:", operator)
        print("Digital product is:", result)
    return (result, operator)
def division(a,b):
    #parameter - 2 integers a and b (both between 1 and 3999 included) that will be the 2 roman numerals convert to integers to do the arithmetic.
    #return - the operator (/) and the result of the division in the range 1 and 3999 both included. 

    operator = "/"
    quotient = a // b
    remainder = a % b
    if quotient < 1 or quotient > 3999:
        if remainder > 0 or remainder < 3999:
            print("Operator:", operator)
            print(f"Digital quotient is OUT OF RANGE and the remainder is: {remainder}")
    elif remainder < 1 or remainder > 3999:
        if quotient > 0 or quotient < 3999:
            print("Operator:", operator)
            print(f"Digital quotient is: {quotient} and the remainder is OUT OF RANGE")
    elif quotient < 1 or quotient > 3999:
        if remainder < 1 or remainder > 3999:
            print("Operator:", operator)
            print("Digital quotient and remainder are OUT OF RANGE")
    elif quotient > 0 or quotient < 3999:
        if remainder > 0 or remainder < 3999:
            print("Operator:", operator)
            print(f"Digital quotient is: {quotient} and the the remainder is: {remainder}")
    return (quotient, remainder, operator)
def power(a,b):
    #parameter - 2 integers a and b (both between 1 and 3999 included) that will be the 2 roman numerals convert to integers to do the arithmetic.
    #return - the operator (^) and the result of the power in the range 1 and 3999 both included. 
    operator = "^"
    result = a ** b
    if result < 1 or result > 3999:
        print("Operator:", operator)
        print("The digital result for the power is OUT OF RANGE")
    else:
        print("Operator:", operator)
        print("Digital result of the power is:", result)
    return (result, operator)
def convert_to_roman(num):
    #parameter - num is an integer >0 and < 3999.
    #return -  roman_result is a string with valid roman letters corresponding to the integer value.

    if num < 1 or num > 3999:
        return "OUT OF RANGE(No conversion to roman)"
    else:
        thousands = ["","M","MM","MMM"]
        hundreds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        if num >= 1000:
            roman_result = thousands[num//1000] + hundreds[(num// 100) % 10] + tens[(num % 100) // 10] + ones[num % 10]
        else:
            roman_result = thousands[num//1000] + hundreds[num// 100] + tens[(num % 100) // 10] + ones[num % 10]
        return roman_result
def integer_to_roman(num,operator,num2=0):
    #parameter - num and num2 are integers and operator is the operator uses to do the arithmetic. num2 has a default number of 0 for the cases that won't need it because num2 will be used as the remainderin the division case.
    #return - no return.This function is really used for the strings instructions with the call of the function convert_to_roman.
    if operator == "+":
        print("Roman Sum is:", convert_to_roman(num))
    elif operator == "-":
        print("Roman Difference is:", convert_to_roman(num))
    elif operator == "*":
        print("Roman Product is:", convert_to_roman(num))
    elif operator == "/":
        roman_quotient = convert_to_roman(num)
        roman_remainder = convert_to_roman(num2)
        print(f"Roman Quotient: {roman_quotient}, Roman Remainder: {roman_remainder}")
    elif operator == "^":
        print("Roman result of the power is:", convert_to_roman(num))

def main():
    #parameter - no parameter. The main program is used to call most of the functions. 
    #return - no return. The main program is used to call most of the functions.  
    print("Welcome to Moulaye's Roman Calculator. Please follow the instructions displayed on the screen and HAVE FUN !!!")
    print()
    while True:
        integer1, integer2 = get_two_romans()
        operator = get_operator()
        if operator == "+":
            result, operator = addition(integer1, integer2)
            integer_to_roman(result, operator)
        elif operator == "-":
            result, operator = subtraction(integer1, integer2)
            integer_to_roman(result, operator)
        elif operator == "*":
            result, operator = multiplication(integer1, integer2)
            integer_to_roman(result, operator)
        elif operator == "/":
            quotient, remainder, operator = division(integer1,integer2)
            integer_to_roman(quotient, operator, remainder)
        elif operator == "^":
            result, operator = power(integer1,integer2)
            integer_to_roman(result, operator)
        choice = input("If you want to continue press any key or press q to quit:").strip().lower()
        if choice == "q":
            print("Program ended. Thank you!")
            break
if __name__ == "__main__":
    main()
