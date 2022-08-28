def comma(list1):
    str=""
    if len(list1)>1:
        for i in range(0,len(list1)):
            if i<len(list1)-2:
                str+=list1[i]+", "
            if i==len(list1)-2:
                str+=list1[i]+" and "+list1[i+1]
    elif len(list1)==1:
        str=list1[0]
    
    return str
     


spam = ['apples', 'bananas', 'tofu', 'cats']
spam1=['apples']
print(comma(spam))
print(comma(spam1))


