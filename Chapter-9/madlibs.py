file_read= open('Chapter-9/text.txt', 'r')
file_text=file_read.read()

file_read.close()

for word in file_text.split():
    if 'ADJECTIVE' in word:
        new_wrd= input("Enter an Adjective: \n")
        file_text= file_text.replace('ADJECTIVE',new_wrd)
    
    elif 'NOUN' in word:
        new_wrd= input("Enter a Noun: \n")
        file_text= file_text.replace('NOUN',new_wrd)
    
   
    elif 'VERB' in word:
        new_wrd= input("Enter a Verb: \n")
        file_text= file_text.replace('VERB',new_wrd)
    
    elif 'ADVERB' in word:
        new_wrd= input("Enter an Adverb: \n")
        file_text= file_text.replace('ADVERB',new_wrd)
    
file_read=open('Chapter-9/text.txt', 'w')
file_read.write(file_text)
file_read.close()