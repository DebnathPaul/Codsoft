

print("Welcome to Calculater")
print("")
print("For Addition press '+'")
print("For Subtraction press '-'")
print("For Multiplication press '*'")
print("For Division press '/'")
print("")

def  user_input():
    num1=int(input("Enter first Number : "))
    num2=int(input("Enter Second Number : "))
    
    operation=input("Choose an Operation : ")
    if (operation=="+"):
        print("Addition of two Number is : ",num1+num2)
    elif (operation=="-"):
        print("Subtraction of two Number is : ",num1-num2)
    elif (operation=="*"):
        print("Multiplication of two Number is : ",num1*num2)
    elif (operation=="/"):
        print("Division of two Number is : ",num1/num2)

for i in "True":
    user_input()
    
    

    


    
