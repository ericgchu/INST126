def main():
        
    # Take the number which will decide the operation 
    operation = int(input("Please choose a number to complete an operation (on 2 numbers): \n 1: Addition\n 2: Subtraction\n 3: Mutiplication\n 4: Division\n 5: Compute Power To\n 6: Add 3 numbers\n 7: Mutiply 3 numbers\n 8: Subtract 3 numbers\n Enter here: "))
    
    # Take int input 
    number1 = int(input("Please enter the first number:"))
    number2 = int(input("Please enter the second number:"))

    # Compute calculation 
    # Add
    if operation == 1: 
        result = number1 + number2
    
    # Subtract
    elif operation == 2: 
        result = number1 - number2 
        
    # Mutiply
    elif operation == 3: 
        result = number1 * number2 
    
    # Divide
    elif operation == 4: 
        result = number1 / number2    
        
    # Take the power of
    elif operation == 5: 
        result = number1 ** number2 
        
    # Otherwise we know we take 3 int inputs
    else: 
        number3 = int(input("Please enter the third number:"))
        
        # Add 3 numbers
        if operation == 6: 
            result = number1 + number2 + number3
           
        # Mutiply 3 numbers
        elif operation == 7: 
            result = number1 * number2 * number3
        
        # Subtract 3 numbers
        elif operation == 8: 
            result = number1 - number2 - number3

    # Print result
    for i in range(1):
        print("The result is: " + str(result))

main()
