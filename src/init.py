
__version__ = '1.0'


import sys

# print the calculation result
def print_result(op1,op2,result,operator):
    print("{0} {2} {1} = {3}".format(op1,op2,operator,result))

# display the guildine
def print_guide():
    print("1: addition")
    print("2: subtraction")
    print("3: multiplication")
    print("4: division")
    print("5: power")
    print("6: guidline")
    print("7: exit program")

# display the message in case users input the invalid key
def print_no_operation():
    print("You have entered incorrect operator");
    print("Please press 6 for help")

# main control flow    
def main():
    
    print_guide()

    while(1):
        print("---------------------------------------")
        operator = int(input("Enter operation: "))
        
        if(int(operator) >= 1 and int(operator) <= 5):
            """ get the input """
            op1 = int(input("Enter the 1st operand: "))
            op2 = int(input("Enter the 2nd operand: "))

            """Just to make the interpreter happy"""
            result = "undefined"
            str_op = "undefined"
            
            if(operator == 1):
                result = op1 + op2
                str_op = '+'    #addition
            elif(operator == 2):
                result = op1 - op2
                str_op = '-'    #subtraction
            elif(operator == 3):
                result = op1 * op2
                str_op = '*'    #multiplication
            elif(operator == 4):
                result = op1/op2
                str_op = '/'    #division
            elif(operator == 5):
                result = op1**op2
                str_op = '^'    #exponent                
            """Pint out the result"""
            print_result(op1,op2,result,str_op)
        elif(operator == 6):
            print_guide()   #Print out the guidline
        elif(operator == 7):
            print("you are about exiting the program! Thanks for giving a try!!")
            break; #Exit program
        else:
            print_no_operation(); #invalid operation

# call the main function    
if __name__ == '__main__':
    sys.exit(main())