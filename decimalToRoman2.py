#manual algorithm retrieved from https://www.rapidtables.com/convert/number/how-number-to-roman-numerals.html
def convert(num, roman):    
    if num >= 1000:
        roman += "M"
        num = num - 1000
    elif num >= 900:
        roman +="CM"
        num = num - 900
    elif num >= 500:
        roman += "D"
        num = num - 500
    elif num >= 400:
        roman += "CD"
        num = num - 400
    elif num >= 100:
        roman += "C"
        num = num - 100
    elif num >= 90:
        roman += "XC"
        num = num - 90
    elif num >= 50:
        roman += "L"
        num = num - 50
    elif num >= 40:
        roman += "XL"
        num = num - 40
    elif num >= 10:
        roman += "X"
        num = num - 10
    elif num >= 9:
        roman += "IX"
        num = num - 9
    elif num >= 5:
        roman += "V"
        num = num - 5
    elif num is 4:
        roman += "IV"
        num = num - 4
    elif num == 3:
        roman += "III"
        num -= 3
    elif num == 2:
        roman += "II"
        num -= 2
    elif num == 1:
        roman += "I"
        num = num - 1
    return num, roman

def arabic_to_roman(num):
    roman = ''
    while num > 0 :
        num, roman = convert(num, roman)
    return roman

def prompt_for_arabic():
    num = input('Enter the number to convert: \n')
    return int(num)

def main():    
    arabic = prompt_for_arabic()
    roman = arabic_to_roman(arabic)
    print(f'The {arabic} is written as {roman} in roman numerals')

def hello(name):
    print(f'Hello {name}')

#definir los tests de py.test con el prefijo "test_"
def test_1_to_I():
    assert arabic_to_roman(1) == "I"
def test_2_to_II():
    assert arabic_to_roman(2) == "II"    
def test_3_to_III():
    assert arabic_to_roman(3) == "III" 
def test_4_to_IV():
    assert arabic_to_roman(4) == "IV" 
def test_5_to_V():
    assert arabic_to_roman(5) == "V" 
def test_6_to_VI():
    assert arabic_to_roman(6) == "VI" 
def test_7_to_VII():
    assert arabic_to_roman(7) == "VII" 
def test_8_to_VII():
    assert arabic_to_roman(8) == "VIII" 
def test_9_to_IX():
    assert arabic_to_roman(9) == "IX" 
def test_10_to_X():
    assert arabic_to_roman(10) == "X" 
def test_345_to_CCCXLV():
    assert arabic_to_roman(345) == "CCCXLV"
def test_449_to_CDXLIX():
    assert arabic_to_roman(449) == "CDXLIX"
def test_512_to_DXII():
    assert arabic_to_roman(512) == "DXII"
def test_788_to_DCCLXXXVIII():
    assert arabic_to_roman(788) == "DCCLXXXVIII"
def test_894_to_DCCCXCIV():
    assert arabic_to_roman(894) == "DCCCXCIV"
def test_964_to_CMLXIV():
    assert arabic_to_roman(964) == "CMLXIV"
def test_1012_to_MXII():
    assert arabic_to_roman(1012) == "MXII"
def test_1659_to_MDCLIX():
    assert arabic_to_roman(1659) == "MDCLIX"
def test_2834_to_MMDCCCXXXIV():
    assert arabic_to_roman(2834) == "MMDCCCXXXIV"
def test_3666_to_MMMDCLXVI():
    assert arabic_to_roman(3666) == "MMMDCLXVI"



if __name__ == '__main__':
    main()
    