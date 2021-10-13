import directory as d

def action():
    
    do_it = input('What would you like to do add-pwd, get-pwd or get-url: ')
    
    while do_it not in ("get-url", "get-pwd", "add-pwd"):
        do_it =  input('TRY AGAIN: only enter add-pwd, get-pwd or get-url: ')
    
    if do_it.lower() == 'add-pwd':
        return 'add passwords'
    
    elif do_it.lower() == 'get-pwd':
        return 'get passwords'
    
    elif do_it.lower() == 'get-url':
        return 'get URLs'

print("Hello and Welcome to Aarush's Password Manager!\nHere you can:\n    save passwords\n    get passwords for specific URLs\n    and get the URLs for specific passwords")

loop_on = True

while loop_on:
    print("\n\n\n\n")
    
    function = action()
    
    if function == 'get passwords':
        url=input('enter url for which pwd is required: ')
        ans = d.get_pwd(url)
        print(ans)
        
    elif function == 'add passwords':
        url=input('enter url: ')
        pwd=input('Enter password: ')
        
        d.add_pwd(url, pwd)
        
    else:
        pwd=input('Enter password: ')
        
        d.get_url(pwd)
    
    print('Your Function has been executed')

        
        
    