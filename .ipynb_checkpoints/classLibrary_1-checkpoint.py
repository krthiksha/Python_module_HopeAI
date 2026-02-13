class MultipleFunctionsUserDefined():
    def age_category(age):
        if age < 18:
            print("Hello Children!")
            category = "Children" 
        elif (age>18 and age<35):
            print("Hey Adult!")
            category = "Adult"
        elif (age>35 and age<59):
            print("Hey Citizen!")
            category = "Citizen"
        else:
            print("Hey Senior Citizen!")
            category = "Senior Citizen"
        return category

    def OddEven(num):
        if num%2==0:
            Message="Even"
        else:
            Message="Odd"
        return Message

    def addition(a,b):
        add=a+b
        return add
    def subraction(a,b):
        sub=a-b
        return sub
    def multiplication(a,b):
        mul=a*b
        return mul