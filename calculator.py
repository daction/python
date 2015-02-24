#Returns the sum of num1 and num2
def add(num1, num2): #function signature
 return num1 + num2

def main():
 operation = input("what do you want to do (+,-,*,/):")
 if(operation != '+' and operation != '-' and operation != '*' and operation != '/'):
                print("You must enter a valid operation")
 else:
                 var1 = int(input("Enter num1: "))
                 var2 = int(input("Enter num2: "))
                 if(operation == '+'):
                                 print(add(var1, var2))
main()
