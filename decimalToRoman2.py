
#global vars
roman = ""

def addSymbol(symbol):
    global roman
    roman = roman + symbol
    

def convert(num):
    
    if num >= 1000:
        addSymbol("M")
        num = num - 1000
    elif num >= 900:
        addSymbol("CM")
        num = num - 900
    elif num >= 500:
        addSymbol("D")
        num = num - 500
    elif num >= 400:
        addSymbol("DC")
        num = num - 500
    elif num >= 100:
        addSymbol("C")
        num = num - 100
    elif num >= 90:
        addSymbol("XC")
        num = num - 90
    elif num >= 50:
        addSymbol("L")
        num = num - 50
    elif num >= 40:
        addSymbol("XL")
        num = num - 500
    elif num >= 10:
        addSymbol("X")
        num = num - 10
    elif num >= 9:
        addSymbol("IX")
        num = num - 9
    elif num >= 5:
        addSymbol("V")
        num = num - 5
    elif num is 4:
        addSymbol("IV")
        num = num - 4;
    elif num >= 1:
        addSymbol("I")
        num = num - 1
    return num;

print ( "Hello Roman!\n")

num = input('Enter the number to convert: \n')

num =  int(num)


while num > 0 :
    num = convert(num)
    
print (roman)
    
