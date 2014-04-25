import itertools
EN_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
EN_LOWER = "abcdefghijklmnopqrstuvwxyz"
RU_UPPER = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
RU_LOWER = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
DIGITS = "1234567890"
SPACE = " "
PUNCTUATIONS = ",.-!?;:’\"/()"
OPERATORS = "+-*/:^()<>="
ALL_SPECS = "`~!@#$%^&*-_=+\\|/?.>,< '\";:[]{}"
DEFAULT_ABC = EN_LOWER + EN_UPPER + DIGITS + ALL_SPECS
SIMPLE = EN_LOWER + DIGITS + EN_UPPER

def passGenerator(min,max,dictionary):
    out = open('out.txt','w')
    for passlen in range(min,max):
        res = itertools.combinations_with_replacement(dictionary,passlen) # 3 is the length of your result.
        for i in res:
            out.write(''.join(i)+'\n')
    out.close()
#simple
if __name__ == '__main__':
    passGenerator(4,6,SIMPLE)