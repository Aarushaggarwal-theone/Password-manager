from random import randint, shuffle, randrange
import directory as d
from generator_lists import low_letters, high_letters, digits, characters

def generate(pwd_s, url_s):
    len_of_pwd = int(input('How long should the password be: '))
    u_letters = int(input("How many uppercase letters tdo you want: "))
    digit = int(input("How many digits to add to the password: "))
    character = int(input('How many special characters to add to the password: '))
    
    sum_pwd = u_letters + digit + characters
    while len_of_pwd < sum_pwd:
        print(f'Invalid length please increase by {sum_pwd - len_of_pwd} and make it {sum_pwd}: ')
        
        if input('(y/n): ') == 'y':  len_of_pwd == sum_pwd
        else: continue
        
    l_letters = len_of_pwd - sum_pwd
    
    password = ''
    
    for i in range(u_letters):
        password += high_letters[randint(0, len(high_letters))]
        i == int(i)
        
    for j in range(l_letters):
        password += low_letters[randint(0, len(low_letters))]
        
    for k in range(digit):
        password += digits[randint(0, len(digits))]
        
    for l in range(character):
        password += characters[randint(0, len(characters))]
        
    pwd = shuffle(password)
    
    return pwd
        