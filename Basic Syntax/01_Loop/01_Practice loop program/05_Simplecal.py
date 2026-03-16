num1 = int(input("Enter first number: \n"))
num2 = int(input("Enter second number: \n"))

a = input("Choose between + , - , / , * ")



match a:
    case "+":
        print(int(num1) + int(num2))
    case "-":
        print(int(num1) - int(num2))
    case "/":
        print(int(num1) % int(num2))
    case "*":
        print(int(num1) * int(num2))
  
