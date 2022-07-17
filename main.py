from art import logo

#Calculator
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Divide
def divide(n1, n2):
  return n1 / n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

operations = {
  "*": multiply, 
  "/": divide, 
  "+": add, 
  "-": subtract
}
def calculator():
  print(logo)
  num1 = float(input("What is the first number: "))
  for key in operations:
    print(key)
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    
    num2 = float(input("What is the next number: "))
    
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    if input("Do you want to perform another calculation? Type 'y'. ").lower() == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()
    
calculator()