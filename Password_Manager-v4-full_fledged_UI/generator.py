from random import randint, shuffle, randrange
import directory as d
from generator_lists import low_letters, high_letters, digits, characters
import string


def generate():
    len_of_pwd = int(input('How long should the password be: '))
    u_letters = int(input("How many uppercase letters tdo you want: "))
    digit = int(input("How many digits to add to the password: "))
    character = int(input('How many special characters do you want: '))

    sum_pwd = u_letters + digit + character
    while len_of_pwd < sum_pwd:
        print(f'Invalid length please make it {sum_pwd}: ')

        if input('(y/n): ') == 'y':
            len_of_pwd = sum_pwd
            break
        else:
            continue

    l_letters = len_of_pwd - sum_pwd

    password = []

    for i in range(u_letters):
        password.append(high_letters[randint(0, len(high_letters)-1)])
        i == int(i)

    for j in range(l_letters):
        password.append(low_letters[randint(0, len(low_letters)-1)])

    for k in range(digit):
        password.append(digits[randint(0, len(digits)-1)])

    for x in range(character):
        password.append(characters[randint(0, len(characters)-1)])

    shuffle(password)
    pwd = ''
    for i in password:
        pwd += i

    return pwd


def add(pwd, pwd_s, url_s):
    url = input("enter url for which password was generated: ")

    d.add_pwd(url, pwd, url_s, pwd_s)
