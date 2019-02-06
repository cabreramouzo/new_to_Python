def convert(n, roman):    
    return (0, "I")

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


def test_1_to_I():
    assert arabic_to_roman(1) == "I"

def test_2_to_II():
    assert arabic_to_roman(1) == "II"    

if __name__ == '__main__':
    main()
    