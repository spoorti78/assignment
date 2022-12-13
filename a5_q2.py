class Calculator:
    def add(self, num1, num2):
        return num1+num2
    
    def subtract(self, num1, num2):
        return num1-num2
        
    def multiply(self, num1, num2):
        return num1*num2

    def divide(self, num1, num2):
        return num1/num2

#create a calculator object
my_cl = Calculator()

while True:

    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")
    
    choice = int(input("Select operation: "))
    
    #Make sure the user have entered the valid choice
    if choice in (1, 2, 3, 4, 5):
        
        #first check whether user want to exit
        if(choice == 5):
            break
        
        #If not then ask fo the input and call appropiate methods        
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))
        
        if(choice == 1):
            print(num1, "+", num2, "=", my_cl.add(num1, num2))
        elif(choice== 2):
            print(num1, "-", num2, "=", my_cl.subtract(num1,num2))
        elif(choice == 3):
            print(num1, "*", num2, "=", my_cl.multiply(num1,num2))
        elif(choice == 4):
            print(num1, "/", num2, "=", my_cl.divide(num1,num2))
    
    else:
        print("Invalid Input")