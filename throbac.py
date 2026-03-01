

# Moulaye Adama Sdibé
# 10/01/2025
# Programming Checkpoint Projecct 1: Roman Numerals Converter: THROBAC
#----------------------------------------------------------------------------------------------------


#Roman numerlas and their values
roman_numerals = ["I","V","X","L","C","D","M"] 
values = [1,5,10,50,100,500,1000]

# Ask user the inputs and first_R_N means first roman number and etc.
first_R_N = input("Enter First Roman Number(no spaces):").upper().strip()
second_R_N = input("Enter Second Number(no spaces):").upper().strip()
operator = input("Operator:").strip()

#Convertion from Roman Numeral 1 to integer.
integer1 = 0
integer2 = 0
index_first_R_N = 0
index__second_R_N = 0
while index_first_R_N < len(first_R_N):
    current_ch_integer1 = values[roman_numerals.index(first_R_N[index_first_R_N])]# this line will take the index of ch and look for the correspond value in the list values and add to the total.
    if index_first_R_N + 1 < len(first_R_N):
        next_ch_integer1 = values[roman_numerals.index(first_R_N[index_first_R_N + 1])]
        if current_ch_integer1 >= next_ch_integer1:
            integer1 += current_ch_integer1
            index_first_R_N += 1 #this line is going to take the next_ch_integer 
        else:
            integer1 += next_ch_integer1 - current_ch_integer1
            index_first_R_N += 2 #this line is going to take the character after the next_ch_integer
    else:
        integer1 += current_ch_integer1
        index_first_R_N += 1
if integer1 > 379 or integer1 <= 0:
    print("The first Roman Number is OUT OF RANGE")
else:
    print(f"Value of {first_R_N}: {integer1}")

    
#Convertion from Roman Numeral 2 to integer.
while index__second_R_N < len(second_R_N):
    current_ch_integer2 = values[roman_numerals.index(second_R_N[index__second_R_N])]# this line will take the index of ch and look for the correspond value in the list values and add to the total.
    if index__second_R_N + 1 < len(second_R_N):
        next_ch_integer2 = values[roman_numerals.index(second_R_N[index__second_R_N + 1])]
        if current_ch_integer2 >= next_ch_integer2:
            integer2 += current_ch_integer2
            index__second_R_N += 1 #this line is going to take the next_ch_integer 
        else:
            integer2 += next_ch_integer2 - current_ch_integer2
            index__second_R_N += 2 #this line is going to take the character after the next_ch_integer
    else:
        integer2 += current_ch_integer2
        index__second_R_N += 1
if integer2 > 379 or integer2 < 1:
    print("The second Roman Number is OUT OF RANGE")
else:
    print(f"Value of {second_R_N}: {integer2}")


#Arithmetic Calculations:
if operator == "+":
    result = integer1 + integer2
    if result < 1 or result > 379:
        print("Operator:", operator)
        print("The digital sum is OUT OF RANGE")
    else:
        print("Operator:", operator)
        print("Digital sum is:", result)
elif operator == "-" :
    if integer1 > integer2 :
        result = integer1 - integer2    
    else:
        result= integer2 - integer1
    if result < 1 or result > 379:
        print("Operator:", operator)
        print("The digital difference is OUT OF RANGE")
    else:
        print("Operator:", operator)
        print("Digital difference is:", result)
elif operator == "*" :
    result = integer1 * integer2
    if result < 1 or result > 379:
        print("Operator:", operator)
        print("The digital product is OUT OF RANGE")
    else:
        print("Operator:", operator)
        print("Digital product is:", result)
elif operator == "/" :
    quotient = integer1 // integer2
    remainder = integer1 % integer2
    if quotient < 1 or quotient > 379:
        if remainder > 0 or remainder < 379:
            print("Operator:", operator)
            print(f"Digital quotient is OUT OF RANGE and the remainder is: {remainder}")
    elif remainder < 1 or remainder > 379:
        if quotient > 0 or quotient < 379:
            print("Operator:", operator)
            print(f"Digital quotient is: {quotient} and the remainder is OUT OF RANGE")
    elif quotient < 1 or quotient > 379:
        if remainder < 1 or remainder > 379:
            print("Operator:", operator)
            print("Digital quotient and remainder are OUT OF RANGE")
    elif quotient > 0 or quotient < 379:
        if remainder > 0 or remainder < 379:
            print("Operator:", operator)
            print(f"Digital quotient is: {quotient} and the the remainder is: {remainder}")

#Convertion from integer to Roman numeral:
if operator == "+" or operator == "-" or operator == "*":
    if result < 1 or result > 379:
        print("OUT OF RANGE(no conversion to roman)")
    else:
        hundreds = ["","C","CC","CCC"]
        tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        roman_result = hundreds[result // 100] + tens[(result % 100) // 10] + ones[result % 10]
        if operator == "+":
            if result < 1 or result > 379:
                print("OUT OF RANGE(no conversion to roman)")
            else:
                print("Roman Sum is:", roman_result)
        elif operator == "-":
            if result < 1 or result > 379:
                print("OUT OF RANGE(no conversion to roman)")
            else:
                print("Roman difference is:", roman_result)
        elif operator == "*":
            if result < 1 or result > 379:
                print("OUT OF RANGE(no conversion to roman)")
            else:
                print("Roman product is:", roman_result)
if operator == "/":
    if (quotient < 1 or quotient > 379) and (remainder < 1 or remainder > 379):
        print("OUT OF RANGE(no conversion to roman)")   
    else:
        hundreds = ["","C","CC","CCC"]
        tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        roman_quotient = hundreds[quotient // 100] + tens[(quotient % 100) // 10] + ones[quotient % 10]
        roman_remainder = hundreds[remainder // 100] + tens[(remainder % 100) // 10] + ones[remainder % 10]
        if quotient < 1 or quotient > 379:
            print(f"Roman quotient is OUT OF RANGE and the Roman remainder is: {roman_remainder}")
        elif remainder < 1 or remainder > 379:
            print(f"Roman quotient is: {roman_quotient} and the Roman remainder is OUT OF RANGE")
        elif (quotient > 0 or quotient < 379) and (remainder > 0 or remainder < 379): 
            print(f"Roman quotient is: {roman_quotient} and the Roman remainder is: {roman_remainder}")
        elif (quotient < 1 or quotient > 379) and (remainder < 1 or remainder > 379):
            print("The Roman quotient and the Roman Remainder are OUT OF RANGE")
        
    

    
    


