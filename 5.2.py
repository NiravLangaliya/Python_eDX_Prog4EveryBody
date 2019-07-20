"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered,
print out the largest and smallest of the numbers.
If the user enters anything other than a valid number catch it with a
try/except and put out an appropriate message and ignore the number.
Enter 7, 2, bob, 10, and 4 and match the output below.
"""
input_flag=1
largest=None
smallest=None

while(input_flag):
    user_input = input("Enter Number:\n")
    if user_input == 'done':
        input_flag=0
        print ("Maximum is",largest)
        print ("Minimum is",smallest)
        break
    else:
        try:
            input_number = int(user_input)
            if largest is None and smallest is None:
                largest = input_number
                smallest = input_number
            elif input_number > largest:
                largest = input_number
            elif  input_number < smallest:
                smallest = input_number
            else:
                continue
        except:
            print("Invalid input")
            #continue