# Case practice excercise

FirstVar = int(input("What is the First Number? "))
SecondVar = int(input("What is the Second Number? "))
chooseoperator = input("Select an Operator? (+, -, *, /) ")
        

match chooseoperator:

    case "+":
            total =  FirstVar + SecondVar
            print("Your Total is: ", total)
    case "-":
            total = FirstVar - SecondVar
            print("Your Total is: ", total)
    case "*":
            total = FirstVar * SecondVar
            print("Your Total is: ", total)
    case "/":
            while SecondVar == 0:
                    SecondVar = int(input("Second Number is zero please re-enter? "))
            total = FirstVar / SecondVar
            print("Your Total is: ", total)
                        

        
    