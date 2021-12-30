
def addition (first_num,second_num):
        return first_num + second_num
def subsrition (first_num,second_num):
        return first_num - second_num

def multi (first_num,second_num):
        return first_num * second_num
def divi (first_num,second_num):
        return first_num / second_num     


def oparetion(value):
        if value == "+":
            print(addition) 
        elif value == "-":
            return subsrition
        elif value == "*":
            return multi 
        elif value == "/":
            return divi
        else:
            print("sorry I am unable to do this !!")    
while True:
    num1 = int(input("Enter first number :\n"))
    num2 = int(input('Enter second number :\n'))
    action = input('addition\nsubsrition\nmulti,divi\n')
    if action == "no":
        break 
           

    
    print(f"answer{oparetion(action)}")


    
        