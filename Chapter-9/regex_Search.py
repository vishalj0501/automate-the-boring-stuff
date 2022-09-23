import re

file_read= open('Chapter-9/text.txt', 'r')
file_text=file_read.read()


line=input("Enter the line: ")
reg=re.compile(r'')

for i in file_text.split('. '):
    
    text=reg.finditer(i)
    if text!='':
        print(line)
        print(i)
