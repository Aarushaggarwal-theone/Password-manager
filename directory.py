directory = []
url_s = []
pwd_s = []

def add_pwd(url, pwd):
    """Add password to database

    Args:
        url (str): insert the url of website to which the pwd being added belongs to.
        pwd (str): insert the pwd which is to be saved for given url.

    Returns:
        Adds a dict to the database named dictionary and adds url and pwd to the url_s and pwd_s lists respectively]65
    """
    global directory
    url_s.append(url)
    pwd_s.append(pwd)
    
    directory.append({url:pwd})
    
def get_pwd(url):
    """Gets a pwd for specific url

    Args:
        url (str): used to pull pwd
    Returns:
        pwd as string
    """
    global directory
    for url1 in url_s:
        if url1 == url:
            get_pwd_card = directory[url1.index()][url]
    
    return get_pwd_card

def get_url(pwd):
    """Gets all urls for specific pwd

    Args:
        pwd (str): used to pull pwd
    Prints:
        pwd as string
    """
    global directory
    
    for dir in directory:
        for i in url_s:
            if dir[i] == pwd:
                print(i)