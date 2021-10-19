import directory as d
import database
import generator

url_s = []
pwd_s = []

final_list = database.get(pwd_s, url_s)
url_s = final_list[1]
pwd_s = final_list[0]


def action():
    """simple function made to pull action from user outside main loop

    Returns:
        function to be executed as str
    """

    do_it = input('''What would you like to do add-pwd, get-pwd, generate-pwd
                  or
                  get-url: ''')

    while do_it not in ("get-url", "get-pwd", "add-pwd", 'generate-pwd'):
        do_it = input('TRY AGAIN: only enter add-pwd, get-pwd or get-url: ')

    if do_it.lower() == 'add-pwd':
        return 'add password'

    elif do_it.lower() == 'get-pwd':
        return 'get password'

    elif do_it.lower() == 'get-url':
        return 'get URLs'

    else:
        return 'gen password'


print("""Hello and Welcome to Aarush's Password Manager!\nHere you can:\n
        save passwords\n    get passwords for specific URLs\n
                              and get the URLs for specific passwords""")

loop_on = True

while loop_on:
    print("\n\n\n\n")

    function = action()

    if function == 'get password':
        url = input('enter url for which pwd is required: ')
        ans = d.get_pwd(url, url_s, pwd_s)
        print(ans)

    elif function == 'add password':
        url = input('enter url: ')
        pwd = input('Enter password: ')

        d.add_pwd(url, pwd, url_s, pwd_s)

    elif function == 'get URLs':
        pwd = input('Enter password: ')

        ans = d.get_url(pwd, url_s, pwd_s)
        print(ans)

    else:
        password = generator.generate()
        print(password)

        ask123 = input('Would you like to add the generated password: ')
        if ask123 == 'yes':
            url = input("enter url for which password was generated: ")
            d.add_pwd(url, password, url_s, pwd_s)
    print('Your Function has been executed')

    ask = input('\nwould you like to continue "y" or "n": ')
    if ask.lower() == 'y':
        continue

    else:
        loop_on = False
        break

database.store(url_s, pwd_s)
