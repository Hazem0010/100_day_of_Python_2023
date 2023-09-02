# nothing show up when using input alone
print("Hello," + " ")
input("Enter your name! ")

print("\n")

# Function inside function, will execute the inner function first and then go outer to the first function
# 1- print() will determine its arguments, like (hello, whitespace, the result of input() )
# 2- once it detect an inner function, it will execute it first, and the result of it will be parsing to string
# and then included back to the print() as its argument
# 3- after executing the input() and get the input from user, the final and complete print() will lokks like:
# print(hello + whitespace + "user input will be here"), and that what will be executed.
print("Hello" + " " + input("Enter your name again! "))