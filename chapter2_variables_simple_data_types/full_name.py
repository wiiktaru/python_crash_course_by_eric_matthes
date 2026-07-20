# String variables 
first_name = 'john'
last_name = 'doe'

""" In f-string Python formats the string by replacing the named variable in braces with its value 
Letter f is placed before the opening quatation of the string """

full_name = f"{first_name} {last_name}"
print(full_name)

# Example of using f-string to compose a message. Title() method used to format the full_name 
print(f"Hello {full_name.title()}!")

# Example of assignin the f-string composed message to a variable. This makes the final print() call more simple
message = f"Hello {full_name.title()}!"
print(message)

""" Example of whitespace - any nonprinting characters (space, tab, end-of-line sympols). 
 Used to organize output for readability  """

# Whitespace using tab 
print("Python")
print("\tPython")

# Whitespace using line 
print("Languages: \nPython\nC\nJavaScript")

# Combining tab and line as a whitespace
print("Languages: \n\tPython\n\tC\n\tJavaScript")