import re

def passwordCheck(text):
    password=re.compile(r'[a-z]+[A-Z]+[0-9]+|[a-z]+[0-9]+[A-Z]|[A-Z]+[a-z]+[0-9]+|[A-Z]+[0-9]+[a-z]+|[0-9]+[a-z]+[A-Z]+|[0-9]+[A-Z]+[a-z]+')
    if len(text)>=8:
        check=password.findall(text)
    else:
        return 'Password should be atleast 8-characters long'
          
    if len(check)==0:
        return 'Password should contain numbers and Upper&Lower Case charactes'
    
    return 'Strong Password'

in_pass=input("Enter password: ")
print(passwordCheck(in_pass))