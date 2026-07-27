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

# Removing extra whitespace from the rigth side of a string with rstrip() method 
# rstrip() method will remove the extra whitespace only temporary unless you assign the value to a variable 
# lstrip() removes whitespaces from the left side of a string 
favorite_language = "Python "
print(favorite_language)

print(favorite_language.rstrip())

# removing whitespaces from left and right side of a string with a strip() method
# Assigning the stripped string to a value for permanent removal of the whitespaces 
word_with_whitespaces = "  Donald Duck  "
word_without_whitespaces = word_with_whitespaces.strip()
print(word_without_whitespaces)

# Removing URL prefix 'https://'

""" string.removeprefix()-method syntax: 
- string: the original string with the prefix 
- prefix: the group of letters you want to remove from the start of the original string
- return type: a string, that has the specified prefix removed, if the prefix existed - else returns the 
original string   
HOX! 
- method is case-sensitive
- leaves the original string unchanged unless assigned to a variable 
"""

url_with_prefix = 'https://google.com'
url_without_prefix = url_with_prefix.removeprefix('https://')
print(url_without_prefix) 
 
 
