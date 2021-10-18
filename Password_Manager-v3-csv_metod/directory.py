def add_pwd(url, pwd, url_s, pwd_s):
    """Add password to database

    Args:
        url (str): insert the url of website to which the pwd being added belongs to.
        pwd (str): insert the pwd which is to be saved for given url.

    Returns:
        Adds a dict to the database named dictionary and adds url and pwd to the url_s and pwd_s lists respectively]65
    """
    
    url_s.append(url)
    pwd_s.append(pwd)
    
def get_pwd(url, url_s, pwd_s):
    pwd_list = []
    """Gets a pwd for specific url

    Args:
        url (str): used to pull pwd
    Returns:
        pwd as string
    """
    pwd = pwd_s[url_s.index(url)]
    
    return pwd

def get_url(pwd, url_s, pwd_s):
    url_list = []
    """Gets all urls for specific pwd

    Args:
        pwd (str): used to pull pwd
    Prints:
        pwd as string
    """
    
    
    for pwd1 in pwd_s:
        if pwd1 == pwd:
            url_list.append(url_s[pwd_s.index(pwd1)])
            
    return url_list