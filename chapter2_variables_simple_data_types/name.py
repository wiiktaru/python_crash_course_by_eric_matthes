""" A string is a series of characters
In Python, anything inside quotes (single or double) is a string  """

# Changing case using title() method. Title method changes each word to begin with a capital letter
name = 'john doe' 
print(name.title())

# Changing case using upper() and lower() methods. These change the case for all the letters 
# The author says that the lower() method is particularly useful for storing data as you typically
# do not want to trust the capitalization that the user provides. Note to self: check company policy 
print(name.upper())
print(name.lower()) 
