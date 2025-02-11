import re

def valid_FirstName():
  
  pattern="^[A-Z][a-z]{1,}$"
   
  first_name=input("Enter first name:")

  
  if re.match(pattern,first_name):
    print("It is Valid  name")
  else:
    print("It is invalid  name")
valid_FirstName()





def valid_LastName(last_name):
  pattern="^[A-Z][a-z]{2,}$"
  
  
  if re.findall(pattern,last_name):
    print("The last name is valid")
  else:
    print("It is not a valid name")
last_name=input("Enter your name:")
valid_LastName(last_name)



def valid_Email():
  pattern=r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$"
  
  email=input("Enter your email:")
  
  if re.match(pattern,email):
    print("Valid email")
  else:
    print("Not a valid email")
valid_Email()
