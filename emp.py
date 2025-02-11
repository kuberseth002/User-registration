import re

def valid_FirstName():
  
  pattern="^[A-Z][a-z]{1,}$"
   
  first_name=input("Enter first name:")

  
  if re.match(pattern,first_name):
    print("It is Valid  name")
  else:
    print("It is invalid  name")
valid_FirstName()