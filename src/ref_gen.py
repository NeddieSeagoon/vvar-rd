import random
import string

alph = string.ascii_uppercase
num = string.digits

def r(in_list):
    return random.choice(in_list)

def generate_ref_code():
    elems = list([r(alph), r(num), r(alph)])
    return ''.join(elems)

if __name__ == '__main__':
    print(generate_ref_code())