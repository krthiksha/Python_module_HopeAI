class AllClass():
    def Subfields():  #static method
        ai_subfields = ["Machine learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are: ")
        for domain in ai_subfields:
            print(domain)

    def OddEven():
        number = int(input("Enter a number: "))
        print(f"{number} is Even number") if (number%2==0) else print(f"{number} is Odd number")

    def Elegible():
        try:
            gender=input("Your Gender: ").lower()
            age=int(input("Your Age: ")) if gender in ["male","female"] else print("enter valid gender")
            if gender=="male" and age>=21:
                eligibility="ELIGIBLE"
            elif gender=="female" and age>=18:
                eligibility="ELIGIBLE"
            else:
                eligibility=" NOT ELIGIBLE"
            return eligibility
        except ValueError as err:
            print("Please enter a valid age in integer!. Error: ",err)

    def percentage():
        try:
            subject_marks = {}  # store all marks in dictionary
            for i in range(1,6):
                subject_marks[f"subject_{i}"]=int(input(f"Subject_{i} mark: "))
            total_marks = sum(subject_marks.values())
            percentage = total_marks//5
            print("Total: ",total_marks)
            print("Percentage: ",percentage, "%")
        except ValueError as err:
            print("Please enter a valid mark in integer!. Error: ",err)

    def triangle():
        try:
            height=int(input("height of triangle"))
            breadth=int(input("breadth of triangle"))
            area_of_triangle = (height*breadth)/2
            side1=int(input("side1 of triangle"))
            side2=int(input("side2 of triangle"))
            base_side=int(input("base_side of triangle"))
            perimeter_of_triangle=side1+side2+base_side 
            print( "area_of_triangle:  ",area_of_triangle)
            print("perimeter_of_triangle : ",perimeter_of_triangle)
        except ValueError as err:
            print("Please enter a valid data. NOTE: all data's in integer!. Error: ",err)

            