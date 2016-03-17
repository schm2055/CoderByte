#Using the Python language, have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. 
def FirstReverse(str): 
    strlen = len(str)
    strlist = list(str)
    index = strlen - 1
    newstr = ''
    count = 0
    while count < strlen:
    	newstr = newstr + strlist[index]
        index = index - 1
        count = count + 1
        
    return newstr

def FirstReverse2(str):
    return str[::-1]

def FirstReverse3(str):
    return ''.join(reversed(str))
    
userinput = raw_input('Enter String\n')
print FirstReverse(userinput)
print FirstReverse2(userinput)
print FirstReverse3(userinput)